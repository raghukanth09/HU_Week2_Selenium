import time
import unittest
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def test_setUp(self):
        self.driver = webdriver.Chrome("/home/naga_raghunadna/PycharmProjects/HU_selenium/chromedriver")
        self.username="naga.raghunadna@hashedin.com"
        self.password="Raghukanth@09"
        self.driver.get("https://qa.hiway.hashedin.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/p[2]/a").click()  # Clicking on Log in with Google
        user_name_area = self.driver.find_element_by_id("identifierId")
        user_name_area.send_keys(self.username)
        user_name_area.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(4)
        password_area = self.driver.find_element_by_name('password')
        password_area.clear()
        password_area.send_keys(self.password)
        self.driver.implicitly_wait(4)
        password_area.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/a').click()
        # Till login

        time.sleep(10)


    """def test_verify_todays_date_and_timesheet_Date(self): # Task 2 from Assignment
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[contains(text(),'TimeSheet') and @class='ng-scope']").click()
        hiway_date = self.driver.find_element_by_xpath("//span[ @class='mobile-timesheet-date ng-binding']")
        print("#################################3")
        hiway_date=str(hiway_date.text)
        hiway_date=str(hiway_date.rsplit(',', 1)[1])
        today = date.today()
        hiway_date_month=hiway_date[1:4]
        hiway_date_date=hiway_date[5:7]
        currentMonth = str(today.strftime("%B"))[0:3]
        currentDate=str(today.strftime("%d"))
        print("Retrieved date and month is ",hiway_date_date, hiway_date_month)
        print("System date and month is ",currentDate, currentMonth)
        self.assertEquals(hiway_date_date,currentDate)
        self.assertEquals(hiway_date_month,currentMonth)
        print("DONE")

        print("#################################3")
        time.sleep(10)"""


    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()