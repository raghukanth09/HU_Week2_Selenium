import time
import unittest
from selenium import webdriver
from Login import LoginPage
from Task2_Compare_today_date_to_hiway_date import Verify_date
from Hiway_dashboard import Home_Dashboard
from Next_button_disabled import Verify_system_and_hiway_date



class Login_in_Hiway(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/naga_raghunadna/PycharmProjects/HU_selenium/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_hiway(self):
        driver=self.driver
        driver.get("https://qa.hiway.hashedin.com/")

        login= LoginPage(driver)
        login.login_into_hiway()

        dashboard= Home_Dashboard(driver)
        dashboard.click_to_go_into_dashboard_of_hiway()
        time.sleep(5)
        print("Login Is done, Now Going for to chack the first test case")


    # Task 2 from Assignment(Verify the time sheet page has loaded into todays date by default)
    def test_verify_todays_date_and_timesheet_Date(self):
        driver = self.driver
        verifying= Verify_date(driver)
        verifying.verify_hiway_and_system_date()
        time.sleep(5)
        print("#########################")
        print("Task 2 completed")

    # Task 4 (Verify the next button is disabled from todays date)
    def test_next_button_disabled(self):
        driver=self.driver
        next_button_disabed=Verify_system_and_hiway_date(driver)
        next_button_disabed.next_button_disabled()
        print("#################")
        print("Task4 also compelted")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("All the tests are completed Successfully")


if __name__ == "__main__":
    unittest.main()