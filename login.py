from selenium.webdriver.common.by import By
from base import BaseClass


class LoginClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.obj = BaseClass(self.driver, self.delay)
        self.usernames_text = []
        self.password = ""
        self.last_user = ""
        self.user = " "

    def get_details(self):
        un = self.obj.wait_till_vissible((By.XPATH, "//div[@id='login_credentials']")).text
        # print("Element text:", un)
        self.usernames_text = un.split('\n')[1::]
        print("all users fetched: ", self.usernames_text)

        pwd = self.obj.wait_till_vissible((By.XPATH, "//div[@class='login_password']")).text
        self.password = pwd.split('\n')[1::]
        self.last_user = self.usernames_text[-1]
        print(f"password:{self.password} ")
        print(f"last user:{self.last_user} ")

    def login(self):
        login_button = self.obj.wait_till_clickable((By.XPATH, "//input[@id='login-button']"))
        login_button.click()

    def logout(self):
        option_btn = self.obj.wait_till_vissible((By.XPATH, "//button[text()='Open Menu']"))
        option_btn.click()
        logout_btn = self.obj.wait_till_clickable((By.XPATH, "//a[text()='Logout']"))
        logout_btn.click()
        print(f"Successfully logged out as {self.user}!!")

    def validate_all_users(self):
        for self.user in self.usernames_text:
            # login
            username_input = self.obj.wait_till_present((By.XPATH, "//input[@id='user-name']"))
            self.obj.send_k(username_input, self.user)

            password_input = self.obj.wait_till_present((By.XPATH, "//input[@id='password']"))
            self.obj.send_k(password_input, self.password)
            self.login()
            # check if logged in successfully
            try:
                self.obj.wait_till_present((By.ID, "inventory_container"))
                print(f"Successfully logged in as {self.user} :)")
            except:
                print(f"Login for {self.user} failed :(")
                self.driver.refresh()
                continue
            # logout
            if self.user != self.last_user:
                self.logout()
