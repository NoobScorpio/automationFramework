import time
from pages.bing_utils import BingUtils
from resources.constants import BingGlossary


class Test_Bing_Search_Suite:
    def setup_method(self):
        """
        :return:
        """
        self.BingPage = BingUtils()
        self.helper = self.BingPage.helper

    def test_search(self, driver):
        """
        :param driver:
        :return:
        """
        searches = [BingGlossary.SIMPLE_SEARCH, BingGlossary.NUMBERS_SEARCH, BingGlossary.SPECIAL_SEARCH]
        for search in searches:
            driver.get(BingGlossary.Bing_URL)
            self.BingPage.wait_for_loading(driver)
            driver.maximize_window()
            self.BingPage.search(driver, search)
            time.sleep(2)
            res = self.BingPage.get_result(driver)
            assert res


