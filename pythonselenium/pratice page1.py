import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("///home/raghava/Music/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("pavankumar")
driver.find_element_by_name("email").send_keys("pavanraghu97@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("12345678")
driver.find_element_by_css_selector("input[type='checkbox']").click()
dropdowm = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
dropdowm.select_by_index(1)
driver.find_element_by_xpath("//input[@id='inlineRadio2']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
textMatch = driver.find_element_by_css_selector("div[class*='alert-success']").text
print(textMatch)
assert ("Success!" in textMatch)
driver.find_element_by_css_selector("a[href*='shop']").click()
cards = driver.find_elements_by_css_selector(".card-title a")
i = -1
for card in cards:
    i = i+1
    cardtext = card.text
    print(cardtext)
    if cardtext == "Blackberry":
        driver.find_elements_by_css_selector(".card-footer button")[i].click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_css_selector("#country").send_keys("ind")
time.sleep(10)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "india")))
driver.find_element_by_link_text("india").click()




