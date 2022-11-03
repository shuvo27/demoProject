from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://learn.premiumsolutionsbd.com")
driver.find_element(By.XPATH, "//*[@class='btn btn-primary loginBtn']").click()

driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='microfe-popup-login']"))
driver.find_element(By.XPATH, "//*[@class='cursor-pointer']").click()


driver.find_element(By.ID,'input-fname').send_keys("Shuvo Karmakar")
driver.find_element(By.NAME,'email').send_keys("Shuvokarmakar277@gmail.com")
driver.find_element(By.NAME,'password').send_keys("shuvo4321@#")
driver.find_element(By.XPATH, "//*[@class='button-base w-full font-semibold button-solid-primary button-md w-full button-enabled']").click()
