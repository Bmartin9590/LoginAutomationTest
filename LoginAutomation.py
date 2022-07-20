# A script to test my login at IceCreamManDc
# This code uses elements such as: XPaths, Name, CSS Selector
# If my login is successful it will print "success" based on the change of the name at the top of the screen from "Login" to "BRANDON"
# My password is *******'d for obvious security reasons

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://icmdc.herokuapp.com/")
time.sleep(1)

signIn = driver.find_element(By.XPATH, '//span[@class = "font big"]').click()
time.sleep(1)

signIn = driver.find_element(By.XPATH, '//a[@class = "dropdown-item font"]').click()
time.sleep(1)

userName = driver.find_element(By.NAME, "email").send_keys("bmartin@test.com")
time.sleep(1)

passWord = driver.find_element(By.NAME, "password").send_keys("**********")
time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, "button[type = 'button']").click()
time.sleep(1)

uName = driver.find_element(By.XPATH, "//span[text() = 'brandon']").text
time.sleep(3)

if uName == 'BRANDON':
    print("Successful login")
else: 
    print("Fail")