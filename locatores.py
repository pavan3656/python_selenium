import time

from selenium import webdriver
driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.find_element_by_name("email").send_keys("pavankumar")
driver.find_element_by_id("pass").send_keys("12345678")
driver.find_element_by_name("login").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Forgotten password?']").click()
