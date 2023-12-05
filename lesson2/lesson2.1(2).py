from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/get_attribute.html'
    driver.get(URL)
    def calc(x):
         return str(math.log(abs(12*math.sin(int(x)))))
    xElement = driver.find_element(By.XPATH, '//img[@valuex]')
    xElementValuex = xElement.get_attribute('valuex')
    x = xElementValuex
    y = calc(x)

    inputAnswer = driver.find_element(By.XPATH, '// input[ @ id = "answer"]')
    checkboxRobot = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    radioRobotsRule = driver.find_element(By.XPATH, '// input[ @ id = "robotsRule"]')
    buttonSubmit = driver.find_element(By.XPATH, '// button[ @ type = "submit"]')

    inputAnswer.send_keys(y)
    checkboxRobot.click()
    radioRobotsRule.click()
    buttonSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
