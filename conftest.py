from selenium import webdriver
import pytest
from resources.read_config import ReadConfig as Cfg


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome, edge")


@pytest.fixture(scope="function")
def driver(request):
    b_name = request.config.getoption("--browser", default="chrome").lower()
    supported_browsers = [
        "edge",
        "chrome"
    ]
    driver = None
    if b_name in supported_browsers:
        if b_name == 'chrome':
            driver = webdriver.Chrome()
        elif b_name == 'edge':
            driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {b_name}")

    yield driver
    driver.quit()


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
