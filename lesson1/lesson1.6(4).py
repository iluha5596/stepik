import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url = 'http://suninjuly.github.io/registration1.html'

driver.get(url)

# time.sleep(5)
inputFirstName = driver.find_element(By.XPATH, '//*[@name="first_name"]')
inputLastName = driver.find_element(By.XPATH, '//*[@name="last_name"]')
inputCity = driver.find_element(By.XPATH, '//*[@class="form-control city"]')
inputCountry = driver.find_element(By.XPATH, '//*[@id="country"]')
buttonSubmit = driver.find_element(By.XPATH, '//*[text()="Submit"]')

inputFirstName.send_keys('Ivan')
inputLastName.send_keys('Ivanov')
inputCity.send_keys('Moscow')
inputCountry.send_keys('Russia')
buttonSubmit.click()
