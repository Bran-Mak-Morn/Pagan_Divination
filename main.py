from flask import Flask, render_template, url_for, request, redirect
from gods import unknown_god
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import random
import os
from init_database import init_db, VikingGod, CelticGod, SlavicGod
from flask import jsonify
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # severity = DEBUG and higher (all logs)

# Set up FILE handler - for Errors and higher
file_handler = RotatingFileHandler('app_errors.log', maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.ERROR)  # severity =  ERROR and higher
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Set up CONSOLE logging - for Info and higher
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # severity = INFO and higher
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Set up database path
logger.info("Setting up database path")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gods_database.db'
logger.info("Creating SQLAlchemy object for Flask app")
db = SQLAlchemy(app)

# Set up Bootstrap
bootstrap = Bootstrap5(app)


def introduce_god(gender):
    """
    Introduces god or goddess to user.
    :param gender:
    :return: string
    """
    if gender == "M":
        return "Tvůj bůh je"
    elif gender == "F":
        return "Tvá bohyně je"
    else:
        return "Error"


@app.route("/")
def index():
    """
    Main landing page.
    :return: index.html
    """
    return render_template("index.html")


@app.route("/divination/<string:tribe>")
def divination(tribe):
    """
    Divination page.
    :param tribe: string
    :return: divination.html with chosen "god" data
    """
    god_data = unknown_god
    if tribe not in ["viking", "celtic", "slavic"]:
        logger.info(f"Info: Unknown tribe of gods: {tribe}")
        return jsonify({"Info": f"Unknown tribe of gods: {tribe}"}), 400

    if tribe == "viking":
        god_data = random.choice(db.session.query(VikingGod).all())
    elif tribe == "celtic":
        god_data = random.choice(db.session.query(CelticGod).all())
    elif tribe == "slavic":
        god_data = random.choice(db.session.query(SlavicGod).all())

    god_introduction = introduce_god(god_data.gender)
    return render_template("divination.html", divination=god_data, introduction=god_introduction)


@app.route("/contact")
def contact():
    """
    Contact page.
    :return: contact.html
    """
    return render_template("contact.html")


@app.route("/web-app-development")
def web_app_development():
    """
    Web app development page.
    :return: web-app-development.html
    """
    return render_template("web-app-development.html")


@app.route("/get-gods")
def get_gods():
    """
    REST API - returns list of gods from chosen tribe.
    :return: json with list of gods
    """
    tribe = request.args.get('tribe')
    gods = None

    if not tribe:
        logger.warning("Warning: Missing 'tribe' parameter")
        return jsonify({"Warning": "Missing 'tribe' parameter"}), 400
    if tribe not in ["viking", "celtic", "slavic"]:
        logger.warning(f"Warning: Unknown tribe of gods: '{tribe}'")
        return jsonify({"Warning": f"Unknown tribe of gods: '{tribe}' "}), 400

    try:
        if tribe == "viking":
            gods = db.session.query(VikingGod).all()
        elif tribe == "celtic":
            gods = db.session.query(CelticGod).all()
        elif tribe == "slavic":
            gods = db.session.query(SlavicGod).all()
    except Exception as e:
        logger.error(f"Error: Database reading failed: {str(e)}")
        return jsonify({"Error": "Internal server error", "message": "Database reading failed"}), 500

    gods_list = [{"id": god.id, "name": god.name, "gender": god.gender, "description": god.description}
                 for god in gods]
    if gods_list:
        return jsonify({"gods": gods_list}), 200
    else:
        logger.warning(f"Warning: Empty list of gods for tribe: {tribe}")
        return jsonify({"Warning": "No gods found for the specified tribe."}), 200


# Global Error Handlers
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 Web page not found: {str(error)}")
    return jsonify({"Warning": "Web page not found", "message": str(error)}), 404


@app.errorhandler(400)
def bad_request(error):
    logger.error(f"400 Bad Request: {str(error)}")
    return jsonify({"Error": "Bad request", "message": str(error)}), 400


@app.errorhandler(500)
def internal_server_error(error):
    logger.error(f"500 Bad Request: {str(error)}")
    return jsonify({"Error": "Internal server error", "message": str(error)}), 500


if __name__ == "__main__":
    DATABASE_PATH = 'instance/gods_database.db'
    if not os.path.exists(DATABASE_PATH):
        logger.info("Database does not exist. Creating...")
        init_db()
        logger.info("Database created.")
    else:
        logger.info("Database exists. Connecting...")

    app.run(debug=True)
