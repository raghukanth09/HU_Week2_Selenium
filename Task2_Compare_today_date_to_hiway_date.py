import time
from datetime import date


class Verify_date():
    def __init__(self, driver):
        self.driver = driver

    def verify_hiway_and_system_date(self):
        print("STarting Test Case 2")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[contains(text(),'TimeSheet') and @class='ng-scope']").click()
        hiway_date = self.driver.find_element_by_xpath("//span[ @class='mobile-timesheet-date ng-binding']")
        print("#################################3")
        hiway_date = str(hiway_date.text)
        hiway_date = str(hiway_date.rsplit(',', 1)[1])
        today = date.today()
        hiway_date_month = hiway_date[1:4]
        hiway_date_date = hiway_date[5:7]
        currentMonth = str(today.strftime("%B"))[0:3]
        currentDate = str(today.strftime("%d"))
        print("Retrieved date and month is ", hiway_date_date, hiway_date_month)
        print("System date and month is ", currentDate, currentMonth)
        print("DONE")
        print("#################################3")
        time.sleep(5)
