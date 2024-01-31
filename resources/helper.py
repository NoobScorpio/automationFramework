
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

SS_PATH = Path(__file__).parent.parent.resolve() / "screenshots"
LOG_PATH = Path(__file__).parent.parent.resolve() / "logs"
CONFIG_PATH = Path(__file__).parent.parent.resolve() / "config"
REPORTS_PATH = Path(__file__).parent.parent.resolve() / "reports"

class Helper:
    def __init__(self):
        pass

    def find_element_by_name(self, driver: WebDriver, name: str):
        """
        :param driver:
        :param name:
        :return:
        """
        try:
            element: WebElement = driver.find_element(By.NAME, name)
            return element
        except Exception as e:
            print(e)
            print(f'Element by Name:{name} is not found')
            return None

    def find_element_by_id(self, driver: WebDriver, eid: str):
        """
        :param driver:
        :param eid:
        :return:
        """
        try:
            element: WebElement = driver.find_element(By.ID, eid)
            return element
        except Exception as e:
            print(e)
            print(f'Element by ID:{eid} is not found')
            return None

    def find_element_by_xpath(self, driver: WebDriver, xpath: str = ''):
        """
        :param driver:
        :param xpath:
        :return:
        """
        try:
            element: WebElement = driver.find_element(By.XPATH, xpath)
            return element
        except Exception as e:
            print(e)
            print(f'Element by XPATH:{xpath} is not found')
            return None

    def check_element_by_xpath(self, driver: WebDriver, xpath: str = ''):
        """
        :param driver:
        :param xpath:
        :return:
        """
        try:
            element = WebDriverWait(driver, 5).until(  # 5 is the number of seconds to wait
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(e)
            print(f'Element by XPATH:{xpath} is not found')
            return None

    def input_text(self, element: WebElement, text: str):
        """
        :param element:
        :param text:
        :return:
        """
        try:
            element.send_keys(text)
        except Exception as e:
            print(e)
            print(f'{text} is not entered')

    def enter(self, element):
        """
        :param element:
        :return:
        """
        try:
            element.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
            print(f'{element} is not entered')
