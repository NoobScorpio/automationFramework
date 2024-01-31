from resources.logger import Logger
from resources.helper import Helper
from resources.read_config import ReadConfig as Cfg


class TestBase:
    log = Logger.logger()
    helper = Helper()
    tester = Cfg.get_tester()
