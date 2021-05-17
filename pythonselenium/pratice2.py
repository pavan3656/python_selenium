from selenium import webdriver
driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxs))
for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
driver.minimize_window()
driver.close()