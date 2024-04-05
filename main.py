from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base import Base


driver=webdriver.Chrome()

#open
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#login
un=driver.find_element(By.XPATH,"//div[@id='login_credentials']").text
usernames_text = un.split('\n')[1::]
print("all users fetched: ",usernames_text)




user_names=["standard_user","locked_out_user","problem_user","performance_glitch_user","error_user","visual_user"]
password="secret_sauce"

driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(usernames_text[3])
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

#dropdown
dropdown=driver.find_element(By.XPATH,"//select")
dropdown.click()
select = Select(dropdown)
select.select_by_value("hilo")

#third high
all_prices=[]
list1=driver.find_elements(By.XPATH, "(//div[@class='inventory_item_description'])/child::div[@class='pricebar']/div[text()]")
for p in list1:
    all_prices.append(p.text)

third_high=all_prices[2]
print("price list ", all_prices)
print("third highest price  ", third_high)
print('\n')

i=1
for ele in list1:
    price=ele.text
    if price == third_high:
        product_name = driver.find_element(By.XPATH,
                                           f"(//div[@class='inventory_item_description'])[{i}]/div/a/div[text()]").text
        print(f"{i}). {product_name}")
        product_discription = driver.find_element(By.XPATH,
                                                  f"(//div[@class='inventory_item_description'])[{i}]/div/div[@class='inventory_item_desc']").text
        print(f" {product_discription}")
        i+=1
        print('\n')


input()