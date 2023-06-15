from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):
	userNameElement = (By.ID, "login_username")
	userPasswordElement = (By.ID, "login_password")
	loginButtonElement = (By.ID, "login_btn")
	loginErrorElement = (By.XPATH, "//div[@class='body2 error']")
	loginSuccessElement = (By.XPATH, "//button[@title='Avatar Link']")

	def __init__(self, driver, getData):
		self.driver = driver
		self.getData = getData

	def portal(self):
		self.driver.get(self.getData['portal'])

	def loginUser(self):
		self.driver.find_element(*LoginPage.userNameElement).send_keys(self.getData['username'])

	def loginPassword(self):
		self.driver.find_element(*LoginPage.userPasswordElement).send_keys(self.getData['password'])

	def loginSubmit(self):
		self.portal()
		self.loginUser()
		self.loginPassword()
		self.driver.find_element(*LoginPage.loginButtonElement).click()

	def loginError(self):
		return self.driver.find_element(*LoginPage.loginErrorElement)

	def loginSuccess(self):
		self.verifyElementPresence(LoginPage.loginSuccessElement)
		return self.driver.find_element(*LoginPage.loginSuccessElement)
