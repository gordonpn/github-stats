import datetime
import logging
import os
from typing import Any, Dict

from pymongo import MongoClient

logger = logging.getLogger("github_scraper")


class Database:
    instance = None

    def __new__(cls, *args, **kwargs) -> Any:
        if cls.instance is None:
            cls.instance = super().__new__(Database)
            return cls.instance
        return cls.instance

    def __init__(self) -> None:
        self.db_name = os.getenv("MONGO_INITDB_DATABASE")
        self.username = os.getenv("MONGO_NON_ROOT_USERNAME")
        self.password = os.getenv("MONGO_NON_ROOT_PASSWORD")
        self.host = os.getenv("MONGODB_HOST", "mongodb")
        self.connection = self.connect()

    def connect(self) -> Any:
        logger.info("Making connection to mongodb")
        uri: str = f"mongodb://{self.username}:{self.password}@{self.host}:27017/{self.db_name}"
        connection = MongoClient(uri)
        return connection[self.db_name]

    def save_commits(self, days, hours: Dict[str, int]) -> None:
        logger.info("Insert commits per days")
        collection = self.connection.collection["commits_per_days"]
        recorded_time = datetime.datetime.utcnow()
        result = collection.insert_one(document={"time": recorded_time, "data": days})
        logger.info(f"Insertion ID: {result.inserted_id}")
        logger.info("Insert commits per hours")
        collection = self.connection.collection["commits_per_hours"]
        recorded_time = datetime.datetime.utcnow()
        result = collection.insert_one(document={"time": recorded_time, "data": hours})
        logger.info(f"Insertion ID: {result.inserted_id}")

    def save_languages(self, languages: Dict[str, float]) -> None:
        logger.info("Insert languages into database")
        collection = self.connection.collection["languages"]
        recorded_time = datetime.datetime.utcnow()
        result = collection.insert_one(
            document={"time": recorded_time, "data": languages}
        )
        logger.info(f"Insertion ID: {result.inserted_id}")
