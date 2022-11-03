from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=options)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")


driver.find_element(By.NAME,'firstname').send_keys('shuvo')
driver.find_element(By.NAME,'lastname').send_keys('Karmakar')


# driver.find_element(By.ID,'sex-1').click()
gender = driver.find_elements(By.NAME,'sex')
gender[1].click()
# driver.find_element(By.ID,'exp-0').click()
Experience = driver.find_elements(By.NAME,'exp')
Experience[3].click()


professions = driver.find_elements(By.XPATH,'//*[@name="profession"]')

print(len(professions))

for profession in professions:
    if profession.get_attribute('value') == 'Automation Tester':
        profession.click()
        assert profession.is_selected()

# country = Select(driver.find_element(By.ID,'continents'))
# country.deselect_by_visible_text('Africa')

driver.find_element(By.XPATH,'//*[@id="continents"]/option[text()="Africa"]').click()
driver.find_element(By.XPATH,'//*[@name="selenium_commands"]/option[text()="WebElement Commands"]').click()

files = driver.find_element(By.XPATH,'//*[@id="photo"]')
files.send_keys('G:\shuvo.jpg')



# s = driver.find_element_by_xpath("//input[@type='file']")
# #file path specified with send_keys
# s.send_keys("C:\Users\Pictures\Logo.jpg")

# commands = driver.find_element(By.NAME,'selenium_commands')
# driver.execute_script("arguments[2].scrollIntoView();", commands)
# email = driver.find_element(By.XPATH,"//*[@id='input-email']")
#
# email.send_keys('Shuvo@rover.info')
# driver.find_element(By.NAME,'email').send_keys('Shuvo@rover.info')
#
# driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='microfe-popup-login']"))
#
# driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys("Shuvo@rover.info")
# driver.find_element(By.XPATH, "//*[@id='input-password']").send_keys("Ss12345678**")
# driver.find_element(By.XPATH, "//*[@class='button-base w-full font-semibold button-solid-primary button-md w-full button-enabled']").click()

# username = driver.find_element_by_xpath('//*[@id="User"]').send_keys('myusername')
# password = driver.find_element_by_xpath('//*[@id="Pass"]').send_keys('mypassword')
# save =  driver.find_element_by_xpath('//*[@id="formLoginDM"]/div[1]/a').click()
