"""Pagan Divination App configuration."""

from os import environ, path
from dotenv import load_dotenv

# Sets location of ".env" file (in root directory in this case)
# Get the path to the directory containing app_config.py
config_dir = path.abspath(path.dirname(__file__))
# Load .env file located one directory up from config_dir
load_dotenv(path.join(config_dir, '..', '.env'))


class Config:
    """
    Set Flask config variables
    """
    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")

    ENVIRONMENT = environ.get("ENVIRONMENT")
    SECRET_KEY = environ.get("SECRET_KEY")

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False