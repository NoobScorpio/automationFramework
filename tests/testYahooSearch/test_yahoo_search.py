import time
from pages.yahoo_utils import YahooUtils
from resources.constants import YahooGlossary


class Test_Yahoo_Search_Suite:
    def setup_method(self):
        """
        :return:
        """
        self.YahooPage = YahooUtils()
        self.helper = self.YahooPage.helper

    def test_search(self, driver):
        """
        :param driver:
        :return:
        """
        searches = [YahooGlossary.SIMPLE_SEARCH, YahooGlossary.NUMBERS_SEARCH, YahooGlossary.SPECIAL_SEARCH]
        for search in searches:
            driver.get(YahooGlossary.Yahoo_URL)
            self.YahooPage.wait_for_loading(driver)
            driver.maximize_window()
            self.YahooPage.search(driver, search)
            time.sleep(2)
            res = self.YahooPage.get_result(driver)
            assert res


