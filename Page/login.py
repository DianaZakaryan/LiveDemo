from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data


class Login_Page(General_Helper):

    login_btn = (By.XPATH, "//a[text()='Login']")
    username_field = (By.XPATH, "//input[@name='username']")
    password_field = (By.XPATH, "//input[@name='password']")
    btn_signin = (By.XPATH, "//button[text()='Log in']")

    def login(self, username, password):
        self.find_and_click(self.login_btn)
        self.find_and_send_keys(self.username_field, username)
        self.find_and_send_keys(self.password_field, password)
        self.find_and_click(self.btn_signin)