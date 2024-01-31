from selenium import webdriver
import pytest
from resources.read_config import ReadConfig as Cfg


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome, edge")
    parser.addoption("--env", action="store", default="dev", help="Type of Environment: dev, qa, prod")


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

@pytest.fixture(scope="function")
def env(request):
    env_name = request.config.getoption("--env", default="dev").lower()
    supported_env = [
        "dev",
        "qa",
        "prod"
    ]
    driver = None
    if env_name in supported_env:
        yield env_name
    else:
        raise ValueError(f"Unsupported environment: {env_name}")


