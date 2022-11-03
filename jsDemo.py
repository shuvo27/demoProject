import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,'name').send_keys('Shuvo')
print(driver.find_element(By.NAME,'name').text)
print(driver.find_element(By.NAME,'name').get_attribute('value'))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element(By.CSS_SELECTOR,'a[href="/angularpractice/shop"]')
# homeButton = driver.find_element(By.CSS_SELECTOR,'a[href="/angularpractice"]')
driver.execute_script('arguments[0].click();',shopButton)


while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)



