from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/math.html'
    driver.get(URL)
    def calc(x):
         return str(math.log(abs(12*math.sin(int(x)))))
    x_element = driver.find_element(By.XPATH, '//div[@class="form-group"]/label/span[2]')
    x = x_element.text
    y = calc(x)

    inputAnswer = driver.find_element(By.XPATH, '// input[ @ id = "answer"]')
    checkboxRobot = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    radioRobotsRule = driver.find_element(By.XPATH, '// input[ @ id = "robotsRule"]')
    radioPeopleRule = driver.find_element(By.XPATH, '// input[ @ id = "peopleRule"]')
    buttonSubmit = driver.find_element(By.XPATH, '// button[ @ type = "submit"]')

    #Проверка, что просатвлен true у радиобатона
    people_checked = radioPeopleRule.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    inputAnswer.send_keys(y)
    checkboxRobot.click()
    radioRobotsRule.click()
    buttonSubmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
