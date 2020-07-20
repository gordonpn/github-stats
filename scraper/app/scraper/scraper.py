import logging
import os
import sys
from collections import OrderedDict
from datetime import datetime
from typing import Dict, List, Set

from dotenv import load_dotenv
from github import Github
from github.GithubException import GithubException

if sys.version_info < (3, 9):
    from backports.zoneinfo import ZoneInfo
else:
    from zoneinfo import ZoneInfo

from app.database.database import Database

logger = logging.getLogger("github_scraper")


def get_day_string(date: datetime) -> str:
    day_mapping: Dict[int, str] = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    return day_mapping[date.weekday()]


class GithubScraper:
    def __init__(self) -> None:
        load_dotenv(verbose=True)
        self.not_my_repos: List[str] = ["2019", "2020", "cusec.github.io"]
        self.g = Github(os.getenv("GITHUB_TOKEN"))

    def get_languages(self) -> Dict[str, float]:
        language_stats: Dict[str, int] = {}
        language_percentages: Dict[str, float] = {}
        sum_of_bytes: int = 0

        for repo in self.g.get_user().get_repos():
            if repo.name in self.not_my_repos:
                continue
            try:
                for lang, bytes_of_code in repo.get_languages().items():
                    if "typescript" in lang.lower() or "javascript" in lang.lower():
                        lang = "JavaScript/TypeScript"

                    sum_of_bytes += bytes_of_code
                    language_stats[lang] = language_stats.get(lang, 0) + bytes_of_code
            except GithubException as e:
                logger.info(f"{repo.name} {str(e)}")

        for lang, total_bytes in language_stats.items():
            language_percentages[lang] = (total_bytes / sum_of_bytes) * 100

        logger.info(f"Returning {language_percentages=}")
        return language_percentages

    def get_commits(self):
        commit_stats_days: OrderedDict[str, int] = OrderedDict(
            {
                "Sunday": 0,
                "Monday": 0,
                "Tuesday": 0,
                "Wednesday": 0,
                "Thursday": 0,
                "Friday": 0,
                "Saturday": 0,
            }
        )
        commit_stats_hours: Dict[str, int] = {
            "00": 0,
            "01": 0,
            "02": 0,
            "03": 0,
            "04": 0,
            "05": 0,
            "06": 0,
            "07": 0,
            "08": 0,
            "09": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
            "14": 0,
            "15": 0,
            "16": 0,
            "17": 0,
            "18": 0,
            "19": 0,
            "20": 0,
            "21": 0,
            "22": 0,
            "23": 0,
        }
        sum_commits: int = 0
        my_names: List[str] = ["gpnn", "Gordon", "Gordon Pham-Nguyen", "gordonpn"]
        usernames: Set[str] = set()
        for repo in self.g.get_user().get_repos():
            if repo.name in self.not_my_repos:
                continue
            try:
                commits = repo.get_commits()
                for commit in commits:
                    name: str = commit.commit.author.name
                    this_date_unaware: datetime = commit.commit.author.date
                    usernames.add(name)
                    if name not in my_names:
                        continue
                    sum_commits += 1
                    this_date_aware = this_date_unaware.replace(tzinfo=ZoneInfo("UTC"))
                    local_aware = this_date_aware.astimezone(
                        ZoneInfo("America/Montreal")
                    )
                    this_day: str = get_day_string(local_aware)
                    commit_stats_days[this_day] = commit_stats_days.get(this_day, 0) + 1
                    hours_key = str(local_aware.hour)
                    if len(hours_key) == 1:
                        hours_key = f"0{hours_key}"
                    commit_stats_hours[hours_key] = (
                        commit_stats_hours.get(hours_key, 0) + 1
                    )
            except GithubException as e:
                logger.info(f"{repo.name} {str(e)}")

        logger.info(f"Usernames found in commits {usernames}")
        logger.info(f"Total number of commits: {sum_commits}")
        logger.info(f"Returning {commit_stats_days=}")
        logger.info(f"Returning {commit_stats_hours=}")
        return commit_stats_days, commit_stats_hours


def run_commits() -> None:
    github = GithubScraper()
    database = Database()
    data_days, data_hours = github.get_commits()
    database.save_commits(days=data_days, hours=data_hours)


def run_languages() -> None:
    github = GithubScraper()
    database = Database()
    data = github.get_languages()
    database.save_languages(languages=data)
