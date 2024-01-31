import configparser
import os

from resources.helper import CONFIG_PATH

config = configparser.RawConfigParser()
path = os.path.join(CONFIG_PATH, "config.ini")
config.read(path)


class ReadConfig:
    @staticmethod
    def get_tester():
        return config.get('common info', 'tester')
