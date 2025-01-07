import json
from typing import Any, Dict, List
from urllib.parse import quote

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.utils.request import post

valid_categories = [
    'APPLICATION',
    'ANDROID_WEAR',
    'ART_AND_DESIGN',
    'AUTO_AND_VEHICLES',
    'BEAUTY',
    'BOOKS_AND_REFERENCE',
    'BUSINESS',
    'COMICS',
    'COMMUNICATION',
    'DATING',
    'EDUCATION',
    'ENTERTAINMENT',
    'EVENTS',
    'FINANCE',
    'FOOD_AND_DRINK',
    'HEALTH_AND_FITNESS',
    'HOUSE_AND_HOME',
    'LIBRARIES_AND_DEMO',
    'LIFESTYLE',
    'MAPS_AND_NAVIGATION',
    'MEDICAL',
    'MUSIC_AND_AUDIO',
    'NEWS_AND_MAGAZINES',
    'PARENTING',
    'PERSONALIZATION',
    'PHOTOGRAPHY',
    'PRODUCTIVITY',
    'SHOPPING',
    'SOCIAL',
    'SPORTS',
    'TOOLS',
    'TRAVEL_AND_LOCAL',
    'VIDEO_PLAYERS',
    'WATCH_FACE',
    'WEATHER',
    'GAME',
    'GAME_ACTION',
    'GAME_ADVENTURE',
    'GAME_ARCADE',
    'GAME_BOARD',
    'GAME_CARD',
    'GAME_CASINO',
    'GAME_CASUAL',
    'GAME_EDUCATIONAL',
    'GAME_MUSIC',
    'GAME_PUZZLE',
    'GAME_RACING',
    'GAME_ROLE_PLAYING',
    'GAME_SIMULATION',
    'GAME_SPORTS',
    'GAME_STRATEGY',
    'GAME_TRIVIA',
    'GAME_WORD',
    'FAMILY'
]

valid_collections = [
    'topselling_free',
    'topselling_paid',
    'topgrossing'
    ]

def validate(category: str, collection:str ):
    if category in valid_categories and collection in valid_collections:
        return True

    else:
        return False

# Not sure how to add language and country to this search, not sure it works in the node.js version
def lists(
    category: str,
    collection: str,
    num: int = 500,
):

    if validate(category, collection):
        url = Formats.List.build()

        dom = post(
            url,
            Formats.List.build_body(
                num,
                category,
                collection
            ),
            {"content-type": "application/x-www-form-urlencoded"}
        )

        dataset = json.loads(json.loads(dom.splitlines()[3])[0][2])[0][1][0][28][0]

        n_apps = min(len(dataset), num)

        search_results = []

        for app_idx in range(n_apps):
            app = {}
            for k, spec in ElementSpecs.List.items():
                content = spec.extract_content(dataset[app_idx])
                app[k] = content

            search_results.append(app)

        return search_results

    else:
        raise TypeError("Invalid collection or category supplied")
        return []
    

    

