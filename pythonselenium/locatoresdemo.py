import time

from selenium import webdriver
driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_css_selector("input[type='text']").send_keys("6281701553")
driver.find_element_by_name("password").send_keys("6281701553")
driver.find_element_by_xpath("//form[@id='loginForm']/div[1]/div[3]").click()
driver.minimize_window()
driver.close()
