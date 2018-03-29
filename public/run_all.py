import unittest
import os
from comman.file_path import CASE_PATH,REPORT_PATH,INTERFACE_PATH
from public.HTMLTestRunner_PY3 import HTMLTestRunner
from public.mail import Email
# 用例路径
case_path = os.path.join(CASE_PATH, "case")
print(case_path)
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    discover = unittest.defaultTestLoader.discover(CASE_PATH,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    #
    # testsuit = unittest.TestSuite()
    # testsuit.addTest(DeviceList("testGetDeviceList"))


    report = os.path.join(REPORT_PATH,'testGetDeviceList_report.html')
    with open(report, 'wb') as f:

        runner = HTMLTestRunner(f, verbosity=2, title='testGetDeviceList测试', description='testGetDeviceList')
        runner.run(all_case())

    e = Email()
    e.send()