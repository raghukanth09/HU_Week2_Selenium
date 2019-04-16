import time
from TimeSheet_Page import TimeSheet
class Verify_name():
    def __init__(self, driver):
        self.driver = driver

    def verify_name(self):
        driver=self.driver
        get_name= TimeSheet(driver)
        get_name.click_to_go_into_timesheet()
        name_on_screen=get_name.get_on_screen_name()
        name_on_screen=name_on_screen.split('for ')[1].upper()
        print(name_on_screen)
        email_name=get_name.get_email_name()
        email_name=email_name.split('@')[0]
        email_name=email_name.replace('.',' ')
        print(email_name)
        time.sleep(2)

