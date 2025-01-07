import json
from typing import Any, Dict, List
from urllib.parse import quote

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.utils.request import get

def developer(
    devId: str, n_hits: int = 30, lang: str = "en", country: str = "us"
) -> List[Dict[str, Any]]:

    if n_hits <= 0:
        return []

#TO-DO add handling for string developer IDs
    if devId.isnumeric():
        url = Formats.Developer.build(devId=devId, lang=lang, country=country)

        try:
            dom = get(url)
            
        except NotFoundError:
            url = Formats.Searchresults.fallback_build(devId=devId, lang=lang)
            dom = get(url)

        matches = Regex.SCRIPT.findall(dom)  # take out script blocks from dom

        dataset = {}

        for match in matches:
            key_match = Regex.KEY.findall(match)
            value_match = Regex.VALUE.findall(match)

            if key_match and value_match:
                key = key_match[0]
                value = json.loads(value_match[0])

                dataset[key] = value

        try:
            top_result = dataset["ds:3"][0][1][0][21][0]

        except IndexError:
            top_result = None

        success = False

        dataset = dataset["ds:3"][0][1][0][21][0]

        n_apps = min(len(dataset), n_hits)

        search_results = []

        for app_idx in range(n_apps):
            app = {}
            for k, spec in ElementSpecs.Developer.items():
                content = spec.extract_content(dataset[app_idx])
                app[k] = content

            search_results.append(app)

        return search_results

    else:
        raise TypeError("Non-numeric devId supplied")
        return []