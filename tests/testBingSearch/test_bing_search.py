import time
import pytest
from pages.bingPage.bing_page import BingBasePage
import resources.constants as k
from tests.test_base import TestBase
import allure


@allure.severity(allure.severity_level.NORMAL)
class TestBingSearchSuite(TestBase):
    def setup_method(self):
        """
        :return:
        """
        self.BingPage = BingBasePage()
        self.BingPage.set_helper(self.helper)

    @pytest.mark.regression
    def test_search(self, driver):
        """
        :param driver:
        :return:
        """
        self.log.info(f"test_bing_search tested by {self.tester}")
        for search in k.SEARCHES:

            self.log.info("Load Bing URL")
            driver.get(k.BingGlossary.Bing_URL)

            self.log.info("Wait for URL to load")
            self.BingPage.wait_for_loading(driver)
            driver.maximize_window()

            self.log.info(f"Verify search on Bing: {search}")
            self.BingPage.search(driver, search)
            time.sleep(2)
            res = self.BingPage.get_result(driver)

            if res:
                self.log.info(f"PASS: Verify search on Bing: {search}")
                assert res
            else:
                self.capture_screenshot(driver, name=f"test_bing_search")
                self.log.error(f"FAIL: Verify search on Bing: {search}")
                assert False
