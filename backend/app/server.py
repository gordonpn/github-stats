import logging
from logging.config import fileConfig

from dotenv import load_dotenv
from flask import Flask

from app.api.v1.resources.resources import api_bp_v1 as api_v1


def run():
    load_dotenv(verbose=True)
    logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
    logger = logging.getLogger("backend")
    app = Flask(__name__)
    app.register_blueprint(api_v1, url_prefix="/api/v1")
    logger.info("Starting app")
    app.run(debug=False)
