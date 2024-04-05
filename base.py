from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Base:
    def __init__(self):


    def login(self):

        un = driver.find_element(By.XPATH, "//div[@id='login_credentials']").text
        usernames_text = un.split('\n')[1::]
        print("all users fetched: ", usernames_text)