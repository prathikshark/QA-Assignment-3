from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base import BaseClass


# dropdown
class HomeClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.obj = BaseClass(self.driver, self.delay)

    def sort_high_to_low(self):
        dropdown = self.obj.wait_till_vissible((By.XPATH, "//select"))
        dropdown.click()
        select = Select(dropdown)
        select.select_by_value("hilo")

    def get_third_higest(self):
        all_prices = []
        list1 = self.obj.wait_till_all_present(
            (By.XPATH, "(//div[@class='inventory_item_description'])/child::div[@class='pricebar']/div[text()]"))
        for p in list1:
            all_prices.append(p.text)
        third_high = all_prices[2]
        print("price list ", all_prices)
        print("third highest price  ", third_high)
        print('\n')
        i = 1
        for ele in list1:
            price = ele.text
            if price == third_high:
                product_name = self.obj.wait_till_vissible((By.XPATH, f"(//div[@class='inventory_item_description'])[{i}]/div/a/div")).text
                print(f"{i}). {product_name}")
                product_discription = self.obj.wait_till_vissible((By.XPATH,f"(//div[@class='inventory_item_description'])[{i}]/div/div[@class='inventory_item_desc']")).text
                print(f" {product_discription}")
                i += 1
                print('\n')
