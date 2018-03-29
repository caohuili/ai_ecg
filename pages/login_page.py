from public.base_page import BasePage

class LoginPage(BasePage):
    username_box = 'class_name=>Username'
    password_box = 'class_name=>Password'
    login_btn = 'id=>Login'
    login_error_meg= 'id=>PasswordErrorPrompt'
    login_success_meg = 'class_name=>layui-nav-item'

    def type_search(self,text):
        self.type(self.username_box,text)
        #self.type(self.password_box,text)

    def type_login(self,username,password):
        self.type(self.username_box,username)
        self.type(self.password_box,password)

    def send_submit_btn(self):
        self.click(self.login_btn)

    def get_alert_text(self):
        return self.get_alert()

    def get_login_error_meg(self):
        return self.find_element(self.login_error_meg).text

    def get_login_success_meg(self):
        return self.find_element(self.login_success_meg).text