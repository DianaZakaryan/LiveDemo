from selenium import webdriver

class Driver_Lib:

    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    
    def quite_driver(self):
        self.driver.quit()
