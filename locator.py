from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://learn.premiumsolutionsbd.com")
driver.find_element(By.XPATH, "//*[@class='btn btn-primary loginBtn']").click()


# email = driver.find_element(By.XPATH,"//*[@id='input-email']")
#
# email.send_keys('Shuvo@rover.info')
# driver.find_element(By.NAME,'email').send_keys('Shuvo@rover.info')

driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='microfe-popup-login']"))

driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys("Shuvo@rover.info")
driver.find_element(By.XPATH, "//*[@id='input-password']").send_keys("Ss12345678**")
driver.find_element(By.XPATH, "//*[@class='button-base w-full font-semibold button-solid-primary button-md w-full button-enabled']").click()

# username = driver.find_element_by_xpath('//*[@id="User"]').send_keys('myusername')
# password = driver.find_element_by_xpath('//*[@id="Pass"]').send_keys('mypassword')
# save =  driver.find_element_by_xpath('//*[@id="formLoginDM"]/div[1]/a').click()
