"""Pagan Divination Logger & Handlers configuration."""

import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    # Make a folder for logs
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a logger
    logger = logging.getLogger("Pagan Divination")
    logger.setLevel(logging.DEBUG)  # severity = DEBUG and higher (all logs)

    # Set up FILE handler - for Errors and higher
    file_handler = RotatingFileHandler('logs/app_errors.log', maxBytes=1000000, backupCount=5)
    file_handler.setLevel(logging.WARNING)  # severity =  WARNING and higher
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

    return logger
