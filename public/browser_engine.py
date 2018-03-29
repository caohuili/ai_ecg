import configparser
import os
from selenium import webdriver
from public.logger import Logger
from comman.file_path import DRIVERS_PATH,CONFIG_PATH

logger = Logger(logger_name='BrowserEngine').getlog()

CHROMEDRIVER_PATH = os.path.join(DRIVERS_PATH,'chromedriver.exe')

BROWSER_TYPES = {'chrome':webdriver.Chrome}
EXECUTABLE_PATH = {'chrome':CHROMEDRIVER_PATH}


class BrowserEngine:
    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = configparser.ConfigParser()
        config.read(os.path.join(CONFIG_PATH,'config.ini'))

        browser = config.get('browserType','browserName')
        logger.info('You had select %s browser.'%browser)
        url = config.get('testServer','URL')
        logger.info('The test server url is:%s'%url)
        driver = BROWSER_TYPES[browser.lower()](EXECUTABLE_PATH[browser.lower()])
        logger.info('Starting %s browser'%browser)

        driver.get(url)
        logger.info('Open url:%s'%url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        logger.info('Now,Close and quit the browser.')
        self.driver.quit()
