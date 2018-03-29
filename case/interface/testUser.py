import unittest,os,pickle
from uuid import UUID
import paramunittest
from public.logger import Logger
from public.confighttp import ConfigHttp,CONFIG_PATH
from public import base_api

logger =Logger(logger_name='testUserList').getlog()
LocalConfigHttp=ConfigHttp()
devicelist_xls = base_api.get_xls('deviceCase.xlsx','device_list')


@paramunittest.parametrized(*devicelist_xls)
class DeviceList(unittest.TestCase):
    def setParameters(self,case_name,method,pageSize,pageIndex,result,retCode,reason):
        self.case_name = str(case_name)
        self.method = str(method)
        self.pageSize = str(pageSize)
        self.pageIndex = str(pageIndex)
        self.result = str(result)
        self.retCode = str(retCode)
        self.reason = str(reason)
        self.response = None
        self.list = None

    def description(self):
        self.case_name

    def setUp(self):
        pass

    def load_cookies(self,filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)


    def testGetDeviceList(self):
        api_url = base_api.get_api_from_xml('devicelist')
        LocalConfigHttp.set_url(api_url)
        datas = {"pageSize": int(float(self.pageSize)), "pageIndex": int(self.pageIndex)}
        LocalConfigHttp.set_data(datas)
        header = {
            'User-Agent': 'okhttp/3.3.1',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
        }
        LocalConfigHttp.set_headers(header)

        LocalConfigHttp.set_cookies(self.load_cookies('cookies.txt'))
        self.response = LocalConfigHttp.post()
        self.checkResult()

    def tearDown(self):
        pass

    def checkResult(self):
        try:
            logger.info(self.response.text)
            self.devicecontent = self.response.json()
            self.assertEqual(str(self.devicecontent['retCode']),self.retCode)
            self.assertEqual(self.devicecontent['reason'],self.reason)
            logger.info(self.devicecontent['reason'])
            self.devicelist = self.devicecontent['data']['resultList']

            db_devicelist = base_api.get_value_from_db(base_api.get_sql('Backoffice','Device','select_device_list'))

            for i in range(len(self.devicelist)):
                self.assertEqual(self.devicelist[i]['deviceId'],str(db_devicelist[i]['DeviceId']),'fail')
        except Exception as e:
            logger.info(e)


if __name__ == '__main__':
    unittest.main()
    # testsuit = unittest.TestSuite()
    # testsuit.addTest(DeviceList("testGetDeviceList"))
    #
    #
    # report = os.path.join(REPORT_PATH,'testGetDeviceList_report.html')
    # with open(report, 'wb') as f:
    #     runner = HTMLTestRunner(f, verbosity=2, title='testGetDeviceList测试', description='testGetDeviceList')
    #     runner.run(testsuit)
    #
    # e = Email()
    # e.send()


