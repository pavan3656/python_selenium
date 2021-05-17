from selenium import webdriver

driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.maximize_window()
driver.get("https://www.facebook.com/")

driver.get("https://www.facebook.com/go to login page")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

