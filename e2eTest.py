from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
shopButton = driver.find_element(By.CSS_SELECTOR,'a[href="/angularpractice/shop"]')
shopButton.click()

products = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

for product in products:
    productName = product.find_element(By.XPATH,'div/h4/a').text
    if productName == 'Blackberry':
        product.find_element(By.XPATH,'div/button').click()

driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()

driver.find_element(By.XPATH,'//input[@id="country"]').send_keys('ind')
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,'india'))


wait = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))


driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.XPATH,'//input[@class="btn btn-success btn-lg"]').click()
print(driver.find_element(By.CLASS_NAME,'alert-success').text)

driver.get_screenshot_as_file('screenshot.png')