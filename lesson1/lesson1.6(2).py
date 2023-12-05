import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

try:
    url = 'http://suninjuly.github.io/huge_form.html'
    driver.get(url)
    inputElements = driver.find_elements(By.XPATH, '//*[@type="text"]')
    for inputElements in inputElements:
        inputElements.send_keys('Test')
    buttonSubmit = driver.find_element(By.XPATH, '//*[@type="submit"] ')
    buttonSubmit.click()
finally:
    time.sleep(10)
    driver.quit()



