import requests,os,pickle
import configparser
from public.logger import Logger
from comman.file_path import CONFIG_PATH

logger = Logger(logger_name='ConfigHttp').getlog()

class ConfigHttp:
    def __init__(self):
        global url,timeout,login_data
        config = configparser.ConfigParser()
        config.read(os.path.join(CONFIG_PATH,'config.ini'))

        login_data = {
            "appKey": "9B6A5550-1CE9-11E8-ACCF-0ED5F89F718B",
            "userName": "test111",
            "pwdMd5": "1bbd886460827015e5d605ed44252251",
            "selectRole": "1"
        }

        url = config.get('apiDomain','domain')
        timeout = config.get('apiDomain','timeout')
        self.data = {}
        self.url = None
        self.files = {}
        self.headers = {}
        self.cookies = None

    def set_url(self, para_api):
        self.url = url+para_api
        print(self.url)
        return self.url

    def set_headers(self,header):
        self.headers = header

    def set_data(self,data):
        self.data = data

    def set_files(self,file):
        self.files = file

    def set_cookies(self,cookie):
        self.cookies = cookie
    def post(self):
        try:
            response = requests.post(self.url,headers = self.headers,json = self.data,timeout = float(timeout), cookies=self.cookies)
            return response
        except TimeoutError:
            logger.error('TIME OUT %s .'%self.url)




