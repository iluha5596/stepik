from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/execute_script.html'
    driver.get(URL)
    def calc(x):
         return str(math.log(abs(12*math.sin(x))))
    xElement = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = int(xElement.text)
    y = calc(x)

    driver.execute_script("window.scrollBy(0, 150);")
    inputAnswer = driver.find_element(By.XPATH, '// input[ @ id = "answer"]')
    checkboxRobot = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    radioRobotsRule = driver.find_element(By.XPATH, '// input[@id = "robotsRule"]')
    buttonSubmit = driver.find_element(By.XPATH, '// button[@type = "submit"]')

    inputAnswer.send_keys(y)
    checkboxRobot.click()
    radioRobotsRule.click()
    buttonSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
