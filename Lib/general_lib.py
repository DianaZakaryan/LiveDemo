import os
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import logging


class General_Helper():
    
    def __init__(self, driver):
        self.driver = driver
        logging.basicConfig(filename='test.log', format='%(filename)s: %(message)s',
                    level=logging.INFO)

        
    def find(self, loc, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(loc))
            return elem
        except Exception as e:
            logging.error(f"Element not found")

    def find_and_click(self, loc, timeout=60):
        elem = self.find(loc)
        try:
            elem.click()
            logging.info("Element is clickable")
        except Exception as e:
            logging.error("Could not click on element")
    
    def find_and_send_keys(self, loc, text, timeout=60):
        elem = self.find(loc, timeout=timeout)
        try:
            elem.send_keys(text)
        except Exception as e:
            logging.error(f"Could not input {text} in the field")
    
    def find_text(self, loc, timeout=60):
        elem = self.find(loc, timeout=timeout)
        return elem.text

    def get_element_value(self, loc, timeout=60, attempts=3):
        elem = self.find(loc, timeout=timeout)
        while attempts:
            value = elem.get_attribute('value')
            if value:
                return value
            time.sleep(0.3)
            attempts -= 1
           