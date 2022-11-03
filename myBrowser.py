from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://learn.premiumsolutionsbd.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://learn.premiumsolutionsbd.com/s/store")
driver.minimize_window()
driver.maximize_window()
driver.back()
driver.refresh()
driver.get("https://learn.premiumsolutionsbd.com/s/store")
#driver.close()
