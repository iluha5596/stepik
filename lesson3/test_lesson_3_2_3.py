import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()


class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def testAbs1(self):
        URL = 'http://suninjuly.github.io/registration1.html'
        driver.get(URL)
        inputLastNameElement = driver.find_element(By.XPATH, '(//div/label)[2]')
        inputLastName = inputLastNameElement.text
        self.assertEqual(inputLastName, 'Last name*', f'Ожидалось наличие поля "Last name*"')

    def testAbs2(self):
        SecondURL = 'http://suninjuly.github.io/registration2.html'
        driver.get(SecondURL)
        inputLastNameElement = driver.find_element(By.XPATH, '(//div/label)[2]')
        inputLastName = inputLastNameElement.text
        self.assertEqual(inputLastName, 'Last name*', f'Ожидалось наличие поля "Last name*"')


if __name__ == '__main__':
    unittest.main()
