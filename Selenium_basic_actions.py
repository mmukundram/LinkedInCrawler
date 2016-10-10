from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display
import os
import unittest

class LoginTest(unittest.TestCase):
	def setUp(self):
		display = Display(visible=0, size=(800,600))
		display.start()
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.facebook.com")

	def test_Login(self):
		driver = self.driver
		facebookUserName = "mmukundram@gmail.com"
		facebookPassword = "Kunju1994!"
		emailFieldID = "email"
		passFieldID = "pass"
		loginButtonXpath = "//input[@value='Log In']"

		emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
		passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
		loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

		emailFieldElement.clear()
		emailFieldElement.send_keys(facebookUserName)

		passFieldElement.clear()
		passFieldElement.send_keys(facebookPassword)

		loginButtonElement.click()
		fbLogoXpath = "(//a[contains(@href,'logo')])[1]"
		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))	

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
