import os
import pprint
from typing import Dict, List

from dotenv import load_dotenv
from github import Github


def run():
    language_stats_per_repo: Dict[str, Dict[str, int]] = {}
    language_stats: Dict[str, int] = {}
    language_percentages: Dict[str, str] = {}
    sum_of_bytes: int = 0
    not_my_repos: List[str] = ["2019", "2020", "cusec.github.io"]

    load_dotenv(verbose=True)
    g = Github(os.getenv("GITHUB_TOKEN"))

    for repo in g.get_user().get_repos():
        try:
            language_stats_per_repo[repo.name] = repo.get_languages()
        except Exception as e:
            print(str(e))

    for name, lang_stats in language_stats_per_repo.items():
        if name in not_my_repos:
            continue
        for lang, bytes_of_code in lang_stats.items():
            sum_of_bytes += bytes_of_code
            language_stats[lang] = language_stats.get(lang, 0) + bytes_of_code

    for lang, total_bytes in language_stats.items():
        language_percentages[lang] = f"{round((total_bytes / sum_of_bytes) * 100, 2)}%"

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(language_percentages)
