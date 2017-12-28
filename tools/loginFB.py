from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

def login(username = os.environ['FB_UN'], password = os.environ['FB_PW']):
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    
    emailFieldID = "email"
    passFieldID = "pass"
    loginButtonXpath = "//input[@value='Log In']"
    
    while True:
        try:
            email = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))
            pword = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldID))
            login = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
            break
        except:
            print('attempting to find login page...')
    
    email.clear()
    email.send_keys(username)
    pword.clear()
    pword.send_keys(password)
    login.click()
    #finish logging in

    return driver
