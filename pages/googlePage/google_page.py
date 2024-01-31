from pages.base_page import BasePage


class GoogleBasePage(BasePage):
    _google_xpath = "//img[@alt='Google']"
    _result_xpath = "//*[@id='search']//*[contains(@class, 'g ')]//h3"
    _textfield_name = "q"

    def __init__(self):
        self._helper = None

    def set_helper(self, helper):
        self._helper = helper

    def wait_for_loading(self, driver):
        element = self._helper.check_element_by_xpath(driver=driver, xpath=self._google_xpath)
        assert element

    def search(self, driver, text):
        element = self._helper.find_element_by_name(driver=driver, name=self._textfield_name)
        assert element
        element.clear()
        self._helper.input_text(element=element, text=text)
        self._helper.enter(element=element)

    def get_result(self, driver):
        element = self._helper.find_element_by_xpath(driver=driver,
                                                     xpath=self._result_xpath)
        return element.text
