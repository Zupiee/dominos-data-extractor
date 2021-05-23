from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

def get_data(NUMBER):
    webpage = r"https://slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion.ly/" 
    searchterm =  NUMBER
    cd   = os.getcwd()
    driver = webdriver.Chrome(executable_path=r"{}\chromedriver_win32\chromedriver".format(cd))
    driver.get(webpage)
    sbox = driver.find_element(By.ID,"searchbar")
    sbox.send_keys(searchterm)
    submit = driver.find_element(By.ID,"searchbutton")
    submit.click()
    print("__________________")
    l = len(driver.find_element_by_xpath(".//pre").text)
    c = 0
    while (not l ):
        if c > 5:
            print("sumbit")
            driver.refresh()
            sbox = driver.find_element(By.ID,"searchbar")
            sbox.send_keys(searchterm)
            submit = driver.find_element(By.ID,"searchbutton")
            submit.click()
            c=0
        l = len(driver.find_element_by_xpath(".//pre").text)
        time.sleep(2)
        c+=1
    return driver.find_element_by_xpath(".//pre").text
    print("__________________")