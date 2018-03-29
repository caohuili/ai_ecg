import logging
import time,os
from comman.file_path import LOG_PATH

class Logger:
    def __init__(self,logger_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        date_time = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_file_pathname = os.path.join(LOG_PATH,date_time+'.log')

        if not self.logger.handlers:
            fh = logging.FileHandler(log_file_pathname)
            fh.setLevel(logging.INFO)

            console_sh = logging.StreamHandler()
            console_sh.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            console_sh.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(console_sh)

    def getlog(self):
        return self.logger