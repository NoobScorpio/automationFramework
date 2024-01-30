from abc import ABC, abstractmethod


class PageUtils(ABC):

    @abstractmethod
    def wait_for_loading(self, driver):
        pass

    @abstractmethod
    def search(self, driver, text):
        pass

    @abstractmethod
    def get_result(self, driver):
        pass
