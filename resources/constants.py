import os
from typing import final
from pathlib import Path

SEARCHES = [
    "Simple Search By Selenium",
    "0123456789",
    "!@#$%^&*()"
]


@final
class GoogleGlossary:
    GOOGLE_URL = "https://www.google.com/"


@final
class BingGlossary:
    Bing_URL = "https://www.bing.com/"
    DATA_DIR = Path(__file__).parent.parent.resolve() / "testData"
    DATA_FILE = os.path.join(DATA_DIR, "search_data.xlsx")
    SHEET_NAME = "BingData"

@final
class YahooGlossary:
    Yahoo_URL = "https://www.yahoo.com/"

