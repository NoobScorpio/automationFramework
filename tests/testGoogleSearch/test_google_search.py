import time
from pages.google_utils import GoogleUtils
from resources.constants import GoogleGlossary


class Test_Google_Search_Suite:
    def setup_method(self):
        """
        :return:
        """
        self.googlePage = GoogleUtils()
        self.helper = self.googlePage.helper

    def test_search(self, driver):
        """
        :param driver:
        :return:
        """
        searches = [GoogleGlossary.SIMPLE_SEARCH, GoogleGlossary.NUMBERS_SEARCH, GoogleGlossary.SPECIAL_SEARCH]
        for search in searches:
            driver.get(GoogleGlossary.GOOGLE_URL)
            self.googlePage.wait_for_loading(driver)
            driver.maximize_window()
            self.googlePage.search(driver, search)
            time.sleep(2)
            res = self.googlePage.get_result(driver)
            assert res


