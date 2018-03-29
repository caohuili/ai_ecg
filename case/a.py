import requests

import pickle,requests
def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

login_data ={
  "appKey": "9B6A5550-1CE9-11E8-ACCF-0ED5F89F718B",
  "userName": "test111",
  "pwdMd5": "1bbd886460827015e5d605ed44252251",
  "selectRole": "1"
}
r = requests.post('http://ai-ecg.kanebay.com/api/v1/Account/Login',json=login_data)
save_cookies(r.cookies, 'cookies.txt')
url = 'http://ai-ecg.kanebay.com/api/v1/Device/UltraList'
#load cookies and do a request
#requests.post(url, cookies=load_cookies('cookies.txt'))


message = {
  "ECGTestID":"173e1f71-1a84-469f-bc7b-8c039ce32095"
}

message = {
  "pageSize": 5,
  "pageIndex": 0
}
header = {
    'User-Agent': 'okhttp/3.3.1',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/json',
}


response = requests.post(url, json=message, headers=header, cookies=load_cookies('cookies.txt'))
print(response.text)
aa=response.json()
print(len(aa['data']['resultList']))
print()
print(response.json())


