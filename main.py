from flask import Flask, render_template, url_for, request, redirect
from gods import error_god
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import random
import os
from init_database import init_db, VikingGod, CelticGod, SlavicGod
import logging
from flask import jsonify


app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    if tribe == "viking":
        god_data = random.choice(db.session.query(VikingGod).all())
    elif tribe == "celtic":
        god_data = random.choice(db.session.query(CelticGod).all())
    elif tribe == "slavic":
        god_data = random.choice(db.session.query(SlavicGod).all())
    else:
        logger.info("Error god happened")
        god_data = error_god

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
    if not tribe:
        return jsonify({"Error": "Missing 'tribe' parameter"}), 400
    if tribe == "viking":
        print("Viking gods")
        gods = db.session.query(VikingGod).all()
    elif tribe == "celtic":
        gods = db.session.query(CelticGod).all()
    elif tribe == "slavic":
        gods = db.session.query(SlavicGod).all()
    else:
        return jsonify({"Error": f"Unknown tribe: {tribe}"}), 400

    gods_list = [{"id": god.id, "name": god.name, "gender": god.gender, "description": god.description} for god in gods]
    return jsonify({"gods": gods_list}), 200


if __name__ == "__main__":
    DATABASE_PATH = 'instance/gods_database.db'
    if not os.path.exists(DATABASE_PATH):
        logger.info("Database does not exist. Creating...")
        init_db()
        logger.info("Database created.")
    else:
        logger.info("Database exists. Connecting...")

    app.run(debug=True)
