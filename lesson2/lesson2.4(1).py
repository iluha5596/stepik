import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    URL = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(URL)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    buttonBook = driver.find_element(By.XPATH, '//button[@id="book"]')
    buttonBook.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def calc(x):
        return math.log(abs(12*math.sin(x)))
    xElement = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = int(xElement.text)
    y = calc(x)

    inputAnswer = driver.find_element(By.XPATH, '//input[@id="answer"]')
    buttonSubmit = driver.find_element(By.XPATH, '//button[@type="submit"]')

    inputAnswer.send_keys(y)
    buttonSubmit.click()

    alert = driver.switch_to.alert
    alert_text =alert.text
    print('Ответ: ' + alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
