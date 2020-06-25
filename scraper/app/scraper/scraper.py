import logging
import os
from collections import OrderedDict
from datetime import datetime
from typing import Dict, List, Set, Tuple

from backports.zoneinfo import ZoneInfo
from dotenv import load_dotenv
from github import Github
from github.GithubException import GithubException

logger = logging.getLogger("github_scraper")


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
                    sum_of_bytes += bytes_of_code
                    language_stats[lang] = language_stats.get(lang, 0) + bytes_of_code
            except GithubException as e:
                logger.info(f"{repo.name} {str(e)}")

        for lang, total_bytes in language_stats.items():
            language_percentages[lang] = (total_bytes / sum_of_bytes) * 100

        logger.info(f"Returning {language_percentages=}")
        return language_percentages

    def get_commits(self) -> Tuple[OrderedDict[str, int], Dict[int, int]]:
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
        commit_stats_hours: Dict[int, int] = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0,
            16: 0,
            17: 0,
            18: 0,
            19: 0,
            20: 0,
            21: 0,
            22: 0,
            23: 0,
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
                    this_day: str = self.get_day_string(local_aware)
                    commit_stats_days[this_day] = commit_stats_days.get(this_day, 0) + 1
                    commit_stats_hours[local_aware.hour] = (
                        commit_stats_hours.get(local_aware.hour, 0) + 1
                    )
            except GithubException as e:
                logger.info(f"{repo.name} {str(e)}")

        logger.info(f"Usernames found in commits {usernames}")
        logger.info(f"Total number of commits: {sum_commits}")
        logger.info(f"Returning {commit_stats_days=}")
        logger.info(f"Returning {commit_stats_hours=}")
        return commit_stats_days, commit_stats_hours

    def get_day_string(self, date: datetime) -> str:
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
