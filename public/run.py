import os,xlrd
import pandas as pd
import unittest
from public.logger import Logger
import HTMLTestRunner
from public.mail import Email
from comman.file_path import REPORT_PATH,CONFIG_PATH,PUBLIC_PATH,CASE_PATH

logger = Logger('ALLRUN').getlog()

class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
#        resultPath = log.get_report_path()
        # on_off = localReadConfig.get_email("on_off")
        # self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(CASE_PATH, "testCase")
        self.caseFile = None
        self.caseList = []
        self.email = Email().send()

    def set_case_list(self):
        """
        set case list
        :return:
        """
        # fb = open(self.caseListFile)
        # for value in fb.readlines():
        #     data = str(value)
        #     if data != '' and not data.startswith("#"):
        #         self.caseList.append(data.replace("\n", ""))
        # fb.close()
        wb = xlrd.open_workbook(os.path.join(PUBLIC_PATH,'run_case.xls'))
        #sheet = wb.get_sheet_name('Sheet1')



    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        df = pd.read_excel(os.path.join(PUBLIC_PATH,'run_case.xls'))
        self.caseList = df['case_name']


        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            # case_name = case.split("/")[-1]
            # print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(REPORT_PATH+'report.html', 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # # send test report by email
            # if on_off == '':
            #     self.email.send_email()
            # elif on_off == 'off':
            #     logger.info("Doesn't send report email to developer.")
            # else:
            #     logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
