import time

from selenium import webdriver
driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://www.abhibus.com/")
driver.find_element_by_xpath("//input[@id='source']").send_keys("ban")
time.sleep(4)
countries = driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li[1]")
print(len(countries))
for country in countries:
    country.click()
driver.find_element_by_xpath("//input[@id='destination']").send_keys("mad")
time.sleep(2)
countries = driver.find_elements_by_xpath("//ul[@id='ui-id-2']/li[2]")
print(len(countries))
for country in countries:
    country.click()
#driver.minimize_window()

