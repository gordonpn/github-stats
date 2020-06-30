import logging
from logging.config import fileConfig

import pymongo
from flask import Blueprint, make_response
from flask_restful import Api, Resource
from pymongo.cursor import Cursor
from pymongo.errors import ServerSelectionTimeoutError

from app.api.common import Database

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("backend")


def set_headers_json(resp):
    resp.headers["Content-Type"] = "application/json"
    return resp


def get_data(collection):
    database = Database()
    collection = database.connection[database.db_name].collection[collection]
    cursor: Cursor = collection.find().sort("time", pymongo.DESCENDING).limit(1)
    if cursor is None:
        resp = make_response({"message": "not found"}, 404)
        resp = set_headers_json(resp)
        return resp
    resp = make_response(cursor[0]["data"], 200)
    resp = set_headers_json(resp)
    return resp


class Languages(Resource):
    def get(self):
        return get_data("languages")


class CommitsDay(Resource):
    def get(self):
        return get_data("commits_per_days")


class CommitsHours(Resource):
    def get(self):
        return get_data("commits_per_hours")


class HealthCheck(Resource):
    def get(self):
        try:
            database = Database()
            database.connection[database.db_name].command("ping")
        except ServerSelectionTimeoutError as e:
            logger.error("Error with healthcheck")
            logger.error(str(e))
            resp = make_response({"message": "not good"}, 500)
            resp = set_headers_json(resp)
            return resp
        resp = make_response({"message": "all good"}, 200)
        resp = set_headers_json(resp)
        return resp


api_bp_v1 = Blueprint("api_v1", __name__)
api = Api(api_bp_v1)
api.add_resource(Languages, "/languages")
api.add_resource(CommitsDay, "/commits/days")
api.add_resource(CommitsHours, "/commits/hours")
api.add_resource(HealthCheck, "/healthcheck")
