from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/selects1.html'
    driver.get(URL)
    def calc(a, b):
        return str(a + b )
    aElement = driver.find_element(By.XPATH, '//span[@id="num1"]')
    bElement = driver.find_element(By.XPATH, '//span[@id="num2"]')
    a = int(aElement.text)
    b = int(bElement.text)
    x = calc(a, b)

    option = driver.find_element(By.XPATH, f'//option[text() = {x}]')
    buttonSubmit = driver.find_element(By.XPATH, '//button[@type="submit"]')

    option.click()
    buttonSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
