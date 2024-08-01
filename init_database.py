from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.app_config import Config


db_app = Flask(__name__)
db_app.config.from_object(Config)  # Configuring DB

db = SQLAlchemy(db_app)  # Create SQLAlchemy object for Flask app = DB


# TODO change description into "cz-description" column
# TODO turn 3 tables into one DB, add a "tribe" column
# TODO EN Translations for gods, add "en-description" column
""" Models for database table with Viking, Celtic, Slavic tribes """


class God(db.Model):
    """
    Class for Pagan gods table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    tribe = db.Column(db.String(15), nullable=False)
    cz_description = db.Column(db.String(500), nullable=False)
    en_description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<God: {self.name}, tribe: {self.tribe}>'


def db_create_tables():
    """
    Creates tables in the database
    :return: None
    """
    db.create_all()


def convert_to_model(god):
    """
    Converts god object to God model
    :param god:
    :return: VikingGod model
    """
    return God(name=god.name, gender=god.gender, tribe=god.tribe,
               cz_description=god.cz_description, en_description=god.en_description)


def populate_db():
    """
    Populates the database with god models
    :return: None
    """
    from gods import gods
    gods_model = [convert_to_model(god) for god in gods]

    db.session.add_all(gods_model)
    db.session.commit()


def init_db():
    """
    Creates tables in the database and populates with data.
    :return: None
    """
    with db_app.app_context():
        db_create_tables()
        populate_db()
