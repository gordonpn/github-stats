import logging
from logging.config import fileConfig

from flask import Blueprint
from flask_restful import Api, Resource

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("backend")


class Languages(Resource):
    def get(self):
        return {"Not yet": "implemented"}


class CommitsDay(Resource):
    def get(self):
        return {"Not yet": "implemented"}


class CommitsHours(Resource):
    def get(self):
        return {"Not yet": "implemented"}


class HealthCheck(Resource):
    def get(self):
        return {"Not yet": "implemented"}


api_bp_v1 = Blueprint("api_v1", __name__)
api = Api(api_bp_v1)
api.add_resource(Languages, "/languages")
api.add_resource(CommitsDay, "/commits/days")
api.add_resource(CommitsHours, "/commits/hours")
