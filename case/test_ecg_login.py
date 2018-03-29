import unittest,time,os
from public.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from public.HTMLTestRunner_PY3 import HTMLTestRunner
from comman.file_path import REPORT_PATH
from public.mail import Email

class EcgLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ecg_login_username_empty(self):
        '''登录用户名为空'''
        loginpage = LoginPage(self.driver)
        loginpage.type_login('', '123456')
        loginpage.send_submit_btn()
        time.sleep(1)
        # loginpage.get_windows_img()
        login_username_empty_alert = loginpage.get_login_error_meg()

        loginpage.get_windows_img()

        try:
            assert 'Incorrect username or password.' in login_username_empty_alert
            print('test_ecg_login_username_empty is success!')
        except Exception as e:
            print('test_ecg_login_username_empty if failed!', format(e))

    def test_ecg_login_password_empty(self):
        '''登录密码为空'''
        loginpage = LoginPage(self.driver)
        loginpage.type_login('caohuili', '')
        loginpage.send_submit_btn()
        time.sleep(1)
        # loginpage.get_windows_img()
        login_password_empty_alert = loginpage.get_login_error_meg()

        loginpage.get_windows_img()

        try:
            assert 'Incorrect username or password.' == login_password_empty_alert
            print('test_ecg_login_password_empty is success!')
        except Exception as e:
            print('test_ecg_login_password_empty if failed!', format(e))

    def test_ecg_login_userpwd_empty(self):
        '''登录用户名和密码都为空'''
        loginpage = LoginPage(self.driver)
        loginpage.type_login('', '')
        loginpage.send_submit_btn()
        time.sleep(1)
        # loginpage.get_windows_img()
        login_userpwd_empty_alert = loginpage.get_login_error_meg()

        loginpage.get_windows_img()

        try:
            assert 'Incorrect username or password.' == login_userpwd_empty_alert
            print('test_ecg_login_userpwd_empty is success!')
        except Exception as e:
            print('test_ecg_login_userpwd_empty if failed!', format(e))

    def test_ecg_login_userpwd_right(self):
        '''登录用户名和密码正确'''
        loginpage = LoginPage(self.driver)
        loginpage.type_login('test111', '11111111')
        loginpage.send_submit_btn()
        time.sleep(1)
        # loginpage.get_windows_img()
        login_userpwd_empty_alert = loginpage.get_login_success_meg()

        loginpage.get_windows_img()

        try:
            assert len(login_userpwd_empty_alert)>0
            print('test_ecg_login_userpwd_empty is success!')
        except Exception as e:
            print('test_ecg_login_userpwd_empty if failed!', format(e))

    # def test_ecg_login_username_empty(self):
    #     '''登录用户名为空'''
    #     loginpage = LoginPage(self.driver)
    #     loginpage.type_login('','123456')
    #     loginpage.send_submit_btn()
    #     time.sleep(1)
    #     # loginpage.get_windows_img()
    #     login_username_empty_alert = loginpage.get_alert_text()
    #
    #     loginpage.get_windows_img()
    #
    #     try:
    #         assert '账号密码错误' in login_username_empty_alert
    #         print('test_ecg_login_username_empty is success!')
    #     except Exception as e:
    #         print('test_ecg_login_username_empty if failed!',format(e))
    #
    # def test_ecg_login_password_empty(self):
    #     '''登录密码为空'''
    #     loginpage = LoginPage(self.driver)
    #     loginpage.type_login('caohuili','')
    #     loginpage.send_submit_btn()
    #     time.sleep(1)
    #     # loginpage.get_windows_img()
    #     login_password_empty_alert = loginpage.get_alert_text()
    #
    #     loginpage.get_windows_img()
    #
    #     try:
    #         assert '账号密码错误' == login_password_empty_alert
    #         print('test_ecg_login_password_empty is success!')
    #     except Exception as e:
    #         print('test_ecg_login_password_empty if failed!',format(e))
    #
    # def test_ecg_login_userpwd_empty(self):
    #     '''登录用户名和密码都为空'''
    #     loginpage = LoginPage(self.driver)
    #     loginpage.type_login('','')
    #     loginpage.send_submit_btn()
    #     time.sleep(1)
    #     # loginpage.get_windows_img()
    #     login_userpwd_empty_alert = loginpage.get_alert_text()
    #
    #     loginpage.get_windows_img()
    #
    #     try:
    #         assert '请输入账号密码' == login_userpwd_empty_alert
    #         print('test_ecg_login_userpwd_empty is success!')
    #     except Exception as e:
    #         print('test_ecg_login_userpwd_empty if failed!',format(e))

if __name__ == '__main__':
    #unittest.main()
    testsuit = unittest.TestSuite()
    testsuit2 = unittest.TestSuite()
    testsuit.addTest(EcgLogin("test_ecg_login_username_empty"))
    testsuit.addTest(EcgLogin("test_ecg_login_password_empty"))
    testsuit.addTest(EcgLogin("test_ecg_login_userpwd_empty"))
    testsuit.addTest(EcgLogin("test_ecg_login_userpwd_right"))

    report = os.path.join(REPORT_PATH,'login_report.html')
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='ECG登录测试', description='修改html报告')
        runner.run(testsuit)

    e = Email()
    e.send()

