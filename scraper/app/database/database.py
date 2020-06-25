import logging
import os
from typing import Any

import psycopg2

logger = logging.getLogger("github_scraper")


class Database:
    instance = None

    def __new__(cls, *args, **kwargs) -> Any:
        if cls.instance is None:
            cls.instance = super().__new__(Database)
            return cls.instance
        return cls.instance

    def __init__(self) -> None:
        self.db_name = os.getenv("POSTGRES_NONROOT_DB")
        self.username = os.getenv("POSTGRES_NONROOT_USER")
        self.password = os.getenv("POSTGRES_NONROOT_PASSWORD")
        self.host = os.getenv("POSTGRES_HOST", "postgres")
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self) -> Any:
        try:
            connection = psycopg2.connect(
                user=self.username,
                password=self.password,
                host=self.host,
                port="5432",
                database=self.db_name,
            )
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            logger.debug(f"You are connected to: {record}")
            return connection

        except (Exception, psycopg2.Error) as e:
            logger.error("Error while connecting to PostgreSQL")
            logger.error(str(e))

    def close(self) -> None:
        try:
            self.connection.cursor.close()
            self.connection.close()
            logger.debug("PostgreSQL connection is closed")
        except Exception as e:
            logger.error("Error while closing to PostgreSQL")
            logger.error(str(e))

    def save_commits(self):
        pass

    def save_languages(self):
        pass
