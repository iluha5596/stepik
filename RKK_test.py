from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

bseUrl = 'https://rkk-t2.dev.zenit.ru'
link = bseUrl + '/xbpm/runtime/applications/ru.unitarius.zenit/znt-lfr-objects/1.0.0/actions/createRequest?actionParams={"crmClientId":"dghdgh-524-45cv45454","cftClientId":"67974790413"}'

# try:
driver.get(link)
time.sleep(5)
#Авторизация
inputUserName = driver.find_element(By.ID, 'username')
inputPassword = driver.find_element(By.ID, 'password')
buttonEnter = driver.find_element(By.ID, 'kc-login')

inputUserName.send_keys('cm_user14')
inputPassword.send_keys('i39p#ZU*')
buttonEnter.click()

#Короткая анкета
time.sleep(10)
inpitAmount = driver.find_element(By.CSS_SELECTOR, '[field-code="amount"]')
inpitDeclared = driver.find_element(By.NAME, 'incomeDeclared')
buttonSave = driver.find_element(By.XPATH, '//*[text() = "Сохранить"]')

inpitAmount.send_keys('249000')
inpitDeclared.send_keys('90000000')
buttonSave.click()


time.sleep(5)

driver.quit()