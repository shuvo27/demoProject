
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

fireFox_Ops = webdriver.FirefoxOptions()
fireFox_Ops.set_preference("dom.webnotifications.serviceworker.enabled", False)
fireFox_Ops.set_preference("dom.webnotifications.enabled", False)
fireFox_Ops.add_argument('--headless')


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)



driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
