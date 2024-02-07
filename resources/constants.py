import os
from typing import final
from pathlib import Path

import pytest

SEARCHES = [
    "Simple Search By Selenium",
    "0123456789",
    "!@#$%^&*()"
]


@final
class GoogleGlossary:
    GOOGLE_URL_DEV = "https://www.google.com/"
    GOOGLE_URL_QA = "https://www.google.com/"
    GOOGLE_URL_PROD = "https://www.google.com/"

    def get_url(self, env):
        if env == "qa":
            return self.GOOGLE_URL_QA
        elif env == "dev":
            return self.GOOGLE_URL_DEV
        else:
            return self.GOOGLE_URL_PROD


@final
class BingGlossary:
    Bing_URL_DEV = "https://www.bing.com/"
    Bing_URL_QA = "https://www.bing.com/"
    Bing_URL_PROD = "https://www.bing.com/"
    DATA_DIR = Path(__file__).parent.parent.resolve() / "testData"
    DATA_FILE = os.path.join(DATA_DIR, "search_data.xlsx")
    SHEET_NAME = "BingData"

    def get_url(self, env):

        if env == "qa":
            return self.Bing_URL_QA
        elif env == "dev":
            return self.Bing_URL_DEV
        else:
            return self.Bing_URL_PROD


@final
class YahooGlossary:
    Yahoo_URL_DEV = "https://www.yahoo.com/"
    Yahoo_URL_QA = "https://www.yahoo.com/"
    Yahoo_URL_PROD = "https://www.yahoo.com/"

    def get_url(self, env):
        if env == "qa":
            return self.Yahoo_URL_QA
        elif env == "dev":
            return self.Yahoo_URL_DEV
        else:
            return self.Yahoo_URL_PROD
