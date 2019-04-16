class TimeSheet():
    def __init__(self, driver):
        self.driver= driver


    def click_to_go_into_timesheet(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'TimeSheet') and @class='ng-scope']").click()


    def get_on_screen_name(self):
        name_text=self.driver.find_element_by_xpath("//h2[@class='ng-binding']")
        return name_text.text

    def get_email_name(self):
        email_text=self.driver.find_element_by_xpath("//span[@class='username-position hide-sm hide-xs ng-binding ng-scope']")
        return email_text.text