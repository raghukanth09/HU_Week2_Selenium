import time
import unittest
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys

class Home_Dashboard():
    def __init__(self, driver):
        self.driver= driver


    def click_to_go_into_dashboard_of_hiway(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/a').click()
    def logout_from_hiway(self):
        self.driver.find_element_by_xpath("//md-icon[@class='username-position ng-scope material-icons']").click()


