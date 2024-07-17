from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db_app = Flask(__name__)
db_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gods_database.db'  # Set up database in the directory
db = SQLAlchemy(db_app)  # Create SQLAlchemy database object for Flask app


# Models for database tables - Viking, Celtic, Slavic table
class VikingGod(db.Model):
    """
    Class for Viking Gods table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<VikingGod {self.name}>'


class CelticGod(db.Model):
    """
    Class for Celtic Gods table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<CelticGod {self.name}>'


class SlavicGod(db.Model):
    """
    Class for Slavic Gods table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<SlavicGod {self.name}>'


def db_create_tables():
    """
    Creates tables in the database
    :return: None
    """
    db.create_all()


def convert_to_viking_model(viking_god):
    """
    Converts god object to VikingGod model
    :param viking_god:
    :return: VikingGod model
    """
    return VikingGod(name=viking_god.name, gender=viking_god.gender, description=viking_god.description)


def convert_to_celtic_model(celtic_god):
    """
    Converts god object to CelticGod model
    :param celtic_god:
    :return: CelticGod model
    """
    return CelticGod(name=celtic_god.name, gender=celtic_god.gender, description=celtic_god.description)


def convert_to_slavic_model(slavic_god):
    """
    Converts god object to SlavicGod model
    :param slavic_god:
    :return: SlavicGod model
    """
    return SlavicGod(name=slavic_god.name, gender=slavic_god.gender, description=slavic_god.description)


def populate_db():
    """
    Populates the database with god models
    :return: None
    """
    from gods import viking_gods, celtic_gods, slavic_gods

    viking_gods_models = [convert_to_viking_model(god) for god in viking_gods]
    celtic_gods_models = [convert_to_celtic_model(god) for god in celtic_gods]
    slavic_gods_models = [convert_to_slavic_model(god) for god in slavic_gods]

    db.session.add_all(viking_gods_models)
    db.session.add_all(celtic_gods_models)
    db.session.add_all(slavic_gods_models)
    db.session.commit()


def init_db():
    """
    Creates tables in the database and populates with data.
    :return: None
    """
    with db_app.app_context():
        db_create_tables()
        populate_db()
