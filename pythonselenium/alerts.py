from selenium import webdriver
driver = webdriver.Chrome(executable_path="///home/raghava/Music/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
