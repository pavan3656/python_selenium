from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://www.facebook.com/r.php")
driver.find_element_by_name("firstname").send_keys("pavankumar")
driver.find_element_by_name("lastname").send_keys("kumar")
driver.find_element_by_xpath("//input[@name='reg_email__']").send_keys("pavanraghu97@gmail.com")
driver.find_element_by_css_selector("input[data-type='password']").send_keys("12345678")
date = Select(driver.find_element_by_xpath("//select[@name='birthday_day']"))
date.select_by_value("10")
month = Select(driver.find_element_by_xpath("//select[@name='birthday_month']"))
month.select_by_value("5")
year = Select(driver.find_element_by_xpath("//select[@name='birthday_year']"))
year.select_by_value("1999")
radiobutton = driver.find_elements_by_xpath("//span[@class='_5k_2 _5dba']/input")
radiobutton[1].click()
driver.find_element_by_css_selector("button[name='websubmit']").click()








