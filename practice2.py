from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT, 'Click Here').click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)

driver.implicitly_wait(5)
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
tag = driver.find_element(By.TAG_NAME, 'h3').text
assert "Opening a new window" == tag
