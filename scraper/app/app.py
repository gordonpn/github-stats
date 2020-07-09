import logging
import os
import time
from contextlib import ContextDecorator
from logging.config import fileConfig
from typing import Any

import schedule
from dotenv import load_dotenv

from app.healthcheck.healthcheck import HealthCheck, Status
from app.scraper import scraper

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("github_scraper")


class HealthCheckDecorator(ContextDecorator):
    def __enter__(self) -> Any:
        HealthCheck.ping_status(Status.START)
        return self

    def __exit__(self, type_, value, traceback) -> None:
        HealthCheck.ping_status(Status.SUCCESS)


@HealthCheckDecorator()
def update_commits() -> Any:
    logger.info("Running commits update job")
    scraper.run_commits()


@HealthCheckDecorator()
def update_languages() -> Any:
    logger.info("Running language update job")
    scraper.run_languages()


def run_schedule() -> None:
    logger.info("Setting schedule")
    schedule.every(2).days.do(update_commits)
    schedule.every(3).days.do(update_languages)

    logger.info("Job pending")
    while True:
        schedule.run_pending()
        time.sleep(60 * 60)


def run() -> None:
    load_dotenv(verbose=True)
    update_commits()
    time.sleep(1 * 60)
    update_languages()
    if "DEV_RUN" not in os.environ:
        run_schedule()
