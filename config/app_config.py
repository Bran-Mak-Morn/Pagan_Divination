""" Pagan Divination - App configuration """


from os import environ, path
from dotenv import load_dotenv

# locates ".env" file
dotenv_path = path.join(path.dirname(__file__), '../.env')
# Loads .env file variables into environment variables
load_dotenv(dotenv_path)


class Config:
    """
    Set Flask config variables
    """
    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = True

    ENVIRONMENT = environ.get("ENVIRONMENT")
    SECRET_KEY = environ.get("SECRET_KEY")

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
