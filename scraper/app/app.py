import logging
import os
import time
from logging.config import fileConfig

import schedule

logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger("github_scraper")


def update_commits() -> None:
    logger.debug("Running commits update job")


def update_languages() -> None:
    logger.debug("Running language update job")


def run_schedule() -> None:
    logger.debug("Setting schedule")
    schedule.every(2).days.do(update_commits)
    schedule.every(3).days.do(update_languages)

    logger.debug("Job pending")
    while True:
        schedule.run_pending()
        time.sleep(60 * 60)


def run() -> None:
    if "DEV_RUN" in os.environ:
        update_commits()
        update_languages()
    else:
        run_schedule()
