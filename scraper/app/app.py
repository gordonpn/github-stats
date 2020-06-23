import os
import pprint
from datetime import datetime
from typing import Dict, List, Set

from backports.zoneinfo import ZoneInfo
from dotenv import load_dotenv
from github import Github
from github.GithubException import GithubException

# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
# logger = logging.getLogger("github_scraper")

not_my_repos: List[str] = ["2019", "2020", "cusec.github.io"]
load_dotenv(verbose=True)
g = Github(os.getenv("GITHUB_TOKEN"))
pp = pprint.PrettyPrinter(indent=4)


def get_languages() -> None:
    language_stats: Dict[str, int] = {}
    language_percentages: Dict[str, float] = {}
    sum_of_bytes: int = 0

    for repo in g.get_user().get_repos():
        if repo.name in not_my_repos:
            continue
        try:
            for lang, bytes_of_code in repo.get_languages().items():
                sum_of_bytes += bytes_of_code
                language_stats[lang] = language_stats.get(lang, 0) + bytes_of_code
        except GithubException as e:
            print(str(e))

    for lang, total_bytes in language_stats.items():
        language_percentages[lang] = (total_bytes / sum_of_bytes) * 100

    pp.pprint(language_percentages)


def run() -> None:
    commit_stats_days: Dict[str, int] = {}
    commit_stats_hours: Dict[int, int] = {}
    sum_commits: int = 0
    my_names: List[str] = ["gpnn", "Gordon", "Gordon Pham-Nguyen", "gordonpn"]
    usernames: Set[str] = set()
    for repo in g.get_user().get_repos():
        if repo.name in not_my_repos:
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
                local_aware = this_date_aware.astimezone(ZoneInfo("America/Montreal"))
                this_day: str = get_day_string(local_aware)
                commit_stats_days[this_day] = commit_stats_days.get(this_day, 0) + 1
                commit_stats_hours[local_aware.hour] = (
                    commit_stats_hours.get(local_aware.hour, 0) + 1
                )
        except GithubException as e:
            print(str(e))

    pp.pprint(commit_stats_days)
    pp.pprint(commit_stats_hours)
    print(f"Usernames found in commits {usernames}")
    print(f"Total number of commits: {sum_commits}")


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
