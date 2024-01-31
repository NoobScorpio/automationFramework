import logging
from resources.helper import LOG_PATH
import os

import logging

class Logger:
    def __init__(self, file_name):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)

        log_file = os.path.join(LOG_PATH, file_name)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


