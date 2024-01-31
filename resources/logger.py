import logging
from datetime import datetime
from resources.helper import LOG_PATH
import os


class Logger:
    @staticmethod
    def logger():
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)

        log_file = os.path.join(LOG_PATH, "automation.log")
        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        loggen = logging.getLogger()
        loggen.setLevel(logging.INFO)
        return loggen
