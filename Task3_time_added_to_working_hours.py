import time as tm
from datetime import date

class Total_hours_balance():
    def __init__(self, driver):
        self.driver = driver

    def hours_balanced(self):
        print("Starting Test Case 3")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[contains(text(),'TimeSheet') and @class='ng-scope']").click()
        hiway_date = self.driver.find_element_by_xpath("//span[ @class='mobile-timesheet-date ng-binding']")
        hiway_date=str(hiway_date.text)
        total_worked_text_hours_till_now=hiway_date.split(' hrs')[0]
        print(total_worked_text_hours_till_now)
        self.driver.find_element_by_xpath("//input[@type='search' and @aria-label='Project Code']").send_keys("ARU-CCUI-SAL")
        self.driver.find_element_by_xpath("//md-select[@ng-model='newEntry.type']").click()
        self.driver.implicitly_wait(100)
        proj_type= self.driver.find_elements_by_xpath("//md-select-menu[@class = '_md md-overflow']/md-content/md-option")
        proj_type[0].click()
        print("@##Q#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.driver.find_element_by_xpath("//input[@name='newEntry.hrs']").send_keys("2")
        self.driver.find_element_by_xpath("//input[@name='newEntry.min']").send_keys("10")
        self.driver.find_element_by_xpath("//input[@name='newEntry.description']").send_keys("Testing")
        self.driver.find_element_by_xpath("//span[@class='ng-scope']/parent::button[@ng-disabled='!isValid(newEntry)']").click()
        print("Total worked hours befre adding is ",total_worked_text_hours_till_now)
        print("#######################")
        if(total_worked_text_hours_till_now=="00"):
            print("Time is 00")
            minutes=130

        else:
            print("Time is ")
            time=total_worked_text_hours_till_now.split(':')
            hours=int(time[0])
            minutes=int(time[1])
            print(hours)
            print(minutes)
            minutes=minutes+(hours*60)
            minutes=minutes+130
            print("Acutal output coming is ",minutes)
        tm.sleep(10)
        hiway_date_now = self.driver.find_element_by_xpath("//span[ @class='mobile-timesheet-date ng-binding']")
        hiway_date_now = str(hiway_date_now.text)
        current_worked_text_hours_till_now = hiway_date_now.split(' hrs')[0]
        current_worked_text_hours_till_now=current_worked_text_hours_till_now.split(':')
        expected_hours=current_worked_text_hours_till_now[0]
        expected_min=current_worked_text_hours_till_now[1]
        print("Expected hours ",expected_hours)
        print("Expected min ", expected_min)
        expected_min=int(expected_min)+(int(expected_hours)*60)
        print("Expected minutes is",int(expected_min))
        if(int(expected_min)==int(minutes)):
            print("YES")
        else:
            print("No")





