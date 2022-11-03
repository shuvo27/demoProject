import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

list = []
list2 = []


driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('Cu')
time.sleep(4)

count = len(driver.find_elements(By.XPATH, '//div[@class="product"]'))
assert count == 2

buttons = driver.find_elements(By.XPATH, '//div[@class="product-action"]/button')

#//div[@class="product-action"]/button/parent::div/parent::div/h4
for button in buttons:
    list.append(button.find_element(By.XPATH,'parent::div/parent::div/h4').text)
    button.click()
print(list)

driver.find_element(By.XPATH, '//a[@class="cart-icon"]/img').click()
CHECKOUT = driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')
CHECKOUT.click()

wait = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@class="promoCode"]')))
# wait.until(expected_conditions.presence_of_element_located(By.XPATH, '//input[@class="promoCode"]'))
# element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Login")))

veggies = driver.find_elements(By.XPATH,'//p[@class="product-name"]')

for veg in veggies:
    list2.append(veg.text)
print(list2)

assert list == list2



driver.find_element(By.XPATH, '//input[@class="promoCode"]').send_keys('rahulshettyacademy')
promo = driver.find_element(By.XPATH, '//button[@class="promoBtn"]')
promo.click()

wait = WebDriverWait(driver, 10)

promoInfo = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//span[@class="promoInfo"]')))

#

# emailFieldElement = wait.until(lambda driver: driver.find_element_by_id(emailFieldId))
# passFieldElement = wait.until(lambda driver: driver.find_element_by_id(passFieldId))
# loginButtonElement = wait.until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
#
#
# wait2 = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'promoInfo')))
#
# wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, 'promoInfo'))


print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)

print("upadted")
