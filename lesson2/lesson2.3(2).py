import confirm as confirm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/redirect_accept.html'
    driver.get(URL)

    buttonSubmitFirst = driver.find_element(By.XPATH, '//button')
    buttonSubmitFirst.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    def calc(x):
        return math.log(abs(12*math.sin(x)))
    xElement = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = int(xElement.text)
    y = calc(x)

    inputAnswer = driver.find_element(By.XPATH, '//input[@id="answer"]')
    buttonSubmitSecond = driver.find_element(By.XPATH, '//button[@type="submit"]')

    inputAnswer.send_keys(y)
    buttonSubmitSecond.click()

    alert = driver.switch_to.alert
    alert_text =alert.text
    print('Ответ: ' + alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
