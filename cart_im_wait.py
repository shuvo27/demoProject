import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('Cu')
time.sleep(4)

count = len(driver.find_elements(By.XPATH,'//div[@class="product"]'))
assert count == 2

buttons = driver.find_elements(By.XPATH,'//div[@class="product-action"]/button')

for button in buttons:
    button.click()

driver.find_element(By.XPATH,'//a[@class="cart-icon"]/img').click()
button = driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]')
button.click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//input[@class="promoCode"]').send_keys('rahulshettyacademy')
promo = driver.find_element(By.XPATH,'//button[@class="promoBtn"]')
promo.click()