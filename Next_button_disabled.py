import time
import unittest
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys

class Verify_system_and_hiway_date():
    def __init__(self, driver):
        self.driver= driver


    def next_button_disabled(self):
        time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[contains(text(),'TimeSheet') and @class='ng-scope']").click()
        time.sleep(5)
        hiway_prev_but = self.driver.find_element_by_xpath("//span[contains(text(),'prev')]/parent::button")
        hiway_next_button = self.driver.find_element_by_xpath("//span[contains(text(),'next')]/parent::button")
        print("##############")
        time.sleep(5)
        print("Is Next Button enabled for current date -", hiway_next_button.is_enabled())
        print("Is Prev button is enabled for any date ", hiway_prev_but.is_enabled())
        time.sleep(2)