import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pages.bingPage.bing_page import BingBasePage
import resources.constants as k
from tests.test_base import TestBase
from resources.xml_parser import XMLParser
@allure.severity(allure.severity_level.CRITICAL)
class TestBingSearchTDDSuite(TestBase):
    def setup_method(self):
        """
        :return:
        """
        self.BingPage = BingBasePage()
        self.BingPage.set_helper(self.helper)
        self.parser = XMLParser(k.BingGlossary.DATA_FILE, k.BingGlossary.SHEET_NAME)

    @pytest.mark.regression
    def test_search_tdd(self, driver):
        """
        :param driver:
        :return:
        """
        self.log.info(f"test_bing_search_tdd tested by {self.tester}")

        rows, cols = self.parser.get_row_col()
        self.log.info(f"Number of rows:{rows}")
        self.log.info(f"Number of columns:{cols}")
        results = []
        # Skip header row
        for row in range(2, rows+1):

            search = self.parser.read_data(row, 1)
            expected = self.parser.read_data(row, 2)
            self.log.info(f"Data at Row: {row} \n"
                          f"Search: {search}\n"
                          f"Expected: {expected}")

            self.log.info("Load Bing URL")
            driver.get(k.BingGlossary.Bing_URL)

            self.log.info("Wait for URL to load")
            self.BingPage.wait_for_loading(driver)
            driver.maximize_window()

            self.log.info(f"Verify search TDD on Bing: {search}")
            self.BingPage.search(driver, search)
            time.sleep(2)
            res = self.BingPage.get_result(driver)

            if expected == 'Pass':
                if res:
                    self.log.info(f"PASS: Verify search TDD on Bing: {search}")
                    results.append(True)
                else:
                    self.log.error(f"FAIL: Verify search TDD on Bing: {search}")
                    results.append(False)
                    self.capture_screenshot(driver, name=f"test_bing_search_tdd_{row}")
            else:
                if res:
                    self.log.error(f"FAIL: Verify search TDD on Bing: {search}")
                    results.append(False)
                    self.capture_screenshot(driver, name=f"test_bing_search_tdd_{row}")

                else:
                    self.log.info(f"PASS: Verify search TDD on Bing: {search}")
                    results.append(True)

        if False not in results:
            self.log.info(f"Pass: test_bing_search_tdd")
            assert True
        else:
            self.log.info(f"Fail: test_bing_search_tdd")
            assert False

