from selenium.webdriver.common.keys import Keys



class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        self.username = "naga.raghunadna@hashedin.com"
        self.password = "Raghukanth@09"

    def login_into_hiway(self):
        #self.driver.get("https://qa.hiway.hashedin.com/")
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