from pages.page_utils import PageUtils


class GoogleUtils(PageUtils):
    def __init__(self):
        self._helper = None

    def set_helper(self, helper):
        self._helper = helper

    def wait_for_loading(self, driver):
        element = self._helper.check_element_by_xpath(driver=driver, xpath="//img[@alt='Google']")
        assert element

    def search(self, driver, text):
        element = self._helper.find_element_by_name(driver=driver, name="q")
        assert element
        element.clear()
        self._helper.input_text(element=element, text=text)
        self._helper.enter(element=element)

    def get_result(self, driver):
        element = self._helper.find_element_by_xpath(driver=driver,
                                                     xpath="//*[@id='search']//*[contains(@class, 'g ')]//h3")
        return element.text
