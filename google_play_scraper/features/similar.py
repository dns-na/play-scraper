import json
from typing import Any, Dict, List
from urllib.parse import quote
import re
import codecs

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.utils.request import post, get

def similar(
    app_id: str,
    lang: str = "en",
    country: str = "us",
    n_hits: int = 30
):

    # first request finds the gsr query parameter for the supplied application
    url = Formats.Similar.build()
    dom = post(
        url,
        Formats.Similar.build_body(
            app_id
        ),
        {"content-type": "application/x-www-form-urlencoded"}
    )

    result = re.findall(r"cluster\?gsr[^\"']+",dom)[0].rstrip('\\')
    cluster = codecs.decode(result.replace('\\\\','\\'),'unicode_escape')
    gsr = re.findall(r"gsr=([^&]+)", cluster)[0]

    # second request uses the gsr query parameter against the /cluster endpoint
    url = Formats.Similar.build_second(gsr)
    dom = get(url)
    matches = Regex.SCRIPT.findall(dom) # take out script blocks from dom

    dataset = {}
    for match in matches:
        key_match = Regex.KEY.findall(match)
        value_match = Regex.VALUE.findall(match)

        if key_match and value_match:
            key = key_match[0]
            value = json.loads(value_match[0])

            dataset[key] = value

    dataset = dataset["ds:3"][0][1][0][21][0]
    n_apps = min(len(dataset), n_hits)

    search_results = []

    for app_idx in range(n_apps):
        app = {}
        for k, spec in ElementSpecs.Similar.items():
            content = spec.extract_content(dataset[app_idx])
            app[k] = content

        search_results.append(app)

    return search_results    

    return