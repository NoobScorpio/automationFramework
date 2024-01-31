import time

import allure
import pytest

from pages.googlePage.google_page import GoogleBasePage
import resources.constants as k
from tests.test_base import TestBase


@allure.severity(allure.severity_level.NORMAL)
class TestGoogleSearchSuite(TestBase):
    def setup_method(self):
        """
        :return:
        """
        self.googlePage = GoogleBasePage()
        self.googlePage.set_helper(self.helper)

    # Parameterize Tests

    @pytest.mark.sanity
    @pytest.mark.parametrize("search", k.SEARCHES)
    def test_search(self, driver, search):
        """
        :param driver:
        :return:
        """
        self.log.info("test_google_search")

        self.log.info("Load Google URL")
        driver.get(k.GoogleGlossary.GOOGLE_URL)

        self.log.info("Wait for URL to load")
        self.googlePage.wait_for_loading(driver)
        driver.maximize_window()

        self.log.info(f"Verify search on Google: {search}")
        self.googlePage.search(driver, search)
        time.sleep(2)

        res = self.googlePage.get_result(driver)
        if res:
            self.log.info(f"PASS: Verify search on Google: {search}")
            assert res
        else:
            self.log.error(f"FAIL: Verify search on Google: {search}")
            self.capture_screenshot(driver,name="test_google_search")
            assert False
