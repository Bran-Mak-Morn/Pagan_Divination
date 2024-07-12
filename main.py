from flask import Flask, render_template, url_for, request, redirect
from gods import viking_gods, celtic_gods, slavic_gods, error_god
from flask_bootstrap import Bootstrap5
import random


app = Flask(__name__)

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
        god_data = random.choice(viking_gods)
    elif tribe == "celtic":
        god_data = random.choice(celtic_gods)
    elif tribe == "slavic":
        god_data = random.choice(slavic_gods)
    else:
        god_data = error_god

    god_introduction = introduce_god(god_data.gender)
    return render_template("divination.html", divination=god_data, introduction=god_introduction)


@app.route("/kontakt")
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


if __name__ == "__main__":

    app.run(debug=True)
