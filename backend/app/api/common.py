import logging
import os
from logging.config import fileConfig

from dotenv import load_dotenv
from pymongo import MongoClient

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("backend")
load_dotenv(verbose=True)


class Database:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(Database)
            return cls.instance
        return cls.instance

    def __init__(self):
        self.db_name = os.getenv("MONGO_INITDB_DATABASE")
        self.username = os.getenv("MONGO_NON_ROOT_USERNAME")
        self.password = os.getenv("MONGO_NON_ROOT_PASSWORD")
        self.host = os.getenv("MONGODB_HOST", "mongodb")
        self.connection = self.connect()

    def connect(self):
        uri: str = f"mongodb://{self.username}:{self.password}@{self.host}:27017/{self.db_name}"
        connection = MongoClient(uri)
        connection[self.db_name].command("ping")
        return connection
