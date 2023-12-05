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
    url = 'http://suninjuly.github.io/registration1.html'
    driver.get(url)

    inputFirstName = driver.find_element(By.XPATH, '//*[@placeholder="Input your first name"]')
    inputLastName = driver.find_element(By.XPATH, '//*[@placeholder="Input your last name"]')
    inputEmail = driver.find_element(By.XPATH, '//*[@placeholder="Input your email"]')
    buttonSubmit = driver.find_element(By.XPATH, '//*[text() ="Submit"]')

    inputFirstName.send_keys('Ivan')
    inputLastName.send_keys('Ivanov')
    inputEmail.send_keys('mail@mail.ru')
    buttonSubmit.click()

    time.sleep(2)

    welcomeTextElt = driver.find_element(By.TAG_NAME, 'h1')
    welcomeText = welcomeTextElt.text

    assert 'Congratulations! You have successfully registered!' == welcomeText

finally:
    time.sleep(10)
    driver.quit()




