from selenium import webdriver
from login import LoginClass
from home import HomeClass

driver = webdriver.Chrome()
delay = 5
# open
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

login = LoginClass(driver, delay)
login.get_details()
login.validate_all_users()

home = HomeClass(driver, delay)
home.sort_high_to_low()
home.get_third_higest()

input()
