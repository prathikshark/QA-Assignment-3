from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
    def wait_till_vissible(self, locator):
        return WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(locator))

    def wait_till_present(self,locator):
        return WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(locator))

    def wait_till_all_present(self,locator):
        return WebDriverWait(self.driver, self.delay).until(EC.presence_of_all_elements_located(locator))
    def wait_till_clickable(self,locator):
        return WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable(locator))

    def send_k(self,element,data):
        element.send_keys(data)
