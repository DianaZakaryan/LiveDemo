from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data


class Main_Page(General_Helper):

    email_field = (By.XPATH, "//input[@id='email']")
    code_field = (By.XPATH, "//input[@id='code']")
    btn_send = (By.XPATH, "//button[@id='Send']")

    def open_page(self):
        self.driver.get(config_data["url"])

    def pass_security(self):

        self.find_and_send_keys(self.email_field, config_data["email"])
        self.find_and_send_keys(self.code_field, config_data["code"])
        self.find_and_click(self.btn_send)
    