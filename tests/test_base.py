import os

import allure
from allure_commons.types import AttachmentType

from resources.logger import Logger
from resources.helper import Helper, SS_PATH
from resources.read_config import ReadConfig as Cfg


class TestBase:
    log = Logger(file_name="automation.log")
    helper = Helper()
    tester = Cfg.get_tester()

    def capture_screenshot(self, driver, name):
        if not os.path.exists(SS_PATH):
            os.makedirs(SS_PATH)
        file_name = os.path.join(SS_PATH, f"{name}.png")
        driver.get_screenshot_as_file(file_name)
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)
