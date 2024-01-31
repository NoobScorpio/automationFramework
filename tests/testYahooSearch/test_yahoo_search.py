import time

import allure
import pytest

from pages.yahooPage.yahoo_page import YahooBasePage
import resources.constants as k
from tests.test_base import TestBase

@allure.severity(allure.severity_level.MINOR)
class TestYahooSearchSuite(TestBase):
    def setup_method(self):
        """
        :return:
        """
        self.yahooPage = YahooBasePage()
        self.yahooPage.set_helper(self.helper)

    @pytest.mark.regression
    def test_search(self, driver):
        """
        :param driver:
        :return:
        """
        self.log.info("test_yahoo_search")
        for search in k.SEARCHES:

            self.log.info("Load Yahoo URL")
            driver.get(k.YahooGlossary.Yahoo_URL)

            self.log.info("Wait for URL to load")
            self.yahooPage.wait_for_loading(driver)
            driver.maximize_window()

            self.log.info(f"Verify search on Yahoo: {search}")
            self.yahooPage.search(driver, search)
            time.sleep(2)
            res = self.yahooPage.get_result(driver)

            if res:
                self.log.info(f"PASS: Verify search on Yahoo: {search}")
                assert res
            else:
                self.log.error(f"FAIL: Verify search on Yahoo: {search}")
                self.capture_screenshot(driver, name=f"test_yahoo_search")
                assert False



