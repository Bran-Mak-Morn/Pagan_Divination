from flask import Flask, render_template, url_for, request, redirect
from gods import viking_gods, celtic_gods, slavic_gods
from flask_bootstrap import Bootstrap5
import random


app = Flask(__name__)

bootstrap = Bootstrap5(app)


def introduce_god(gender):
    if gender == "M":
        return "Tvůj bůh je"
    else:
        return "Tvá bohyně je"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/divination/<string:tribe>")
def divination(tribe):

    if tribe == "viking":
        god_data = random.choice(viking_gods)
    elif tribe == "celtic":
        god_data = random.choice(celtic_gods)
    elif tribe == "slavic":
        god_data = random.choice(slavic_gods)
    else:
        god_data = "No such god or goddess"
        return render_template("error.html", error=god_data, tribe=tribe)

    god_introduction = introduce_god(god_data.gender)
    return render_template("divination.html", divination=god_data, introduction=god_introduction)


@app.route("/kontakt")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":

    app.run(debug=True)
