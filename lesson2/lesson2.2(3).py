from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    driver = webdriver.Chrome()
    URL = 'https://suninjuly.github.io/file_input.html'
    driver.get(URL)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    inputFirstname = driver.find_element(By.XPATH, '// input[ @ name = "firstname"]')
    inputLastname = driver.find_element(By.XPATH, '// input[ @ name = "lastname"]')
    inputEmail = driver.find_element(By.XPATH, '// input[ @ name = "email"]')
    inputFile = driver.find_element(By.XPATH, '//input[@name="file"]')
    buttonSabmit = driver.find_element(By.XPATH, '//button[@type="submit"]')

    inputFirstname.send_keys('Ivan')
    inputLastname.send_keys('Ivanov')
    inputEmail.send_keys('mail@mail.ru')
    inputFile.send_keys(file_path)
    buttonSabmit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
