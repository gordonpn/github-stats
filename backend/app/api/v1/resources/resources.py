import logging
from logging.config import fileConfig

from flask import Blueprint, make_response
from flask_restful import Api, Resource
from pymongo.errors import ServerSelectionTimeoutError

from app.api.common import Database

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
        try:
            database = Database()
            database.connection[database.db_name].command("ping")
        except ServerSelectionTimeoutError as e:
            logger.error("Error with healthcheck")
            logger.error(str(e))
            resp = make_response({"not": "good"}, 500)
            resp.headers["Content-Type"] = "application/json"
            return resp
        resp = make_response({"message": "all good"}, 200)
        resp.headers["Content-Type"] = "application/json"
        return resp


api_bp_v1 = Blueprint("api_v1", __name__)
api = Api(api_bp_v1)
api.add_resource(Languages, "/languages")
api.add_resource(CommitsDay, "/commits/days")
api.add_resource(CommitsHours, "/commits/hours")
api.add_resource(HealthCheck, "/healthcheck")
