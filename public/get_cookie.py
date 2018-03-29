import pickle,requests,os
from comman.file_path import CASE_PATH


class GetCookie:
    def __init__(self):
        global login_data,login_url
        login_data = {
            "appKey": "9B6A5550-1CE9-11E8-ACCF-0ED5F89F718B",
            "userName": "test111",
            "pwdMd5": "1bbd886460827015e5d605ed44252251",
            "selectRole": "1"
        }
        login_url = 'http://ai-ecg.kanebay.com/api/v1/Account/Login'

    def save_cookies(self,requests_cookiejar):
        with open(os.path.join(CASE_PATH, 'cookies.txt'), 'wb') as f:
            pickle.dump(requests_cookiejar, f)

    def load_cookies(self):
        with open(os.path.join(CASE_PATH, 'cookies.txt'), 'rb') as f:
            return pickle.load(f)

    def get_cookies(self):
        self.r = requests.post(login_url, json=login_data)
        self.save_cookies(self.r.cookies)


# def save_cookies(requests_cookiejar, filename):
#     with open(os.path.join(CASE_PATH,filename), 'wb') as f:
#         pickle.dump(requests_cookiejar, f)
#
# def load_cookies(filename):
#     with open(filename, 'rb') as f:
#         return pickle.load(f)
#
# login_data ={
#   "appKey": "9B6A5550-1CE9-11E8-ACCF-0ED5F89F718B",
#   "userName": "test111",
#   "pwdMd5": "1bbd886460827015e5d605ed44252251",
#   "selectRole": "1"
# }
# r = requests.post('http://ai-ecg.kanebay.com/api/v1/Account/Login',json=login_data)
# save_cookies(r.cookies, 'cookies.txt')