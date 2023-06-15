from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage
from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

	partnerElement = (By.XPATH, "//button[@data-test-id='msps-button']")
	clientElement = (By.XPATH, "//button[@data-test-id='msps-button']")
	partnerInputElement = (By.XPATH, "//input[@data-test-id='msps-search-input']")
	clientInputElement = (By.XPATH, "//input[@data-test-id='clients-search-input']")
	partnerSelectElement = (By.XPATH, "//ul[@data-test-id='msps-list-ul']")
	clientSelectElement = (By.XPATH, "//ul[@data-test-id='clients-list-ul']")
	infrastructureTabElement = (By.XPATH, "//button[@title='Infrastructure']")
	logsLinkElement = (By.XPATH, "//ul/li/a[text()='Logs']")

	def __init__(self, driver, getData):
		self.driver = driver
		self.getData = getData

		loginPage = LoginPage(self.driver, getData)
		loginPage.loginSubmit()

	def selectPartner(self):
		self.verifyElementPresence(HomePage.partnerElement)
		self.driver.find_element(*HomePage.partnerElement).click()
		self.driver.find_element(*HomePage.partnerInputElement).send_keys(self.getData['partner'])
		self.driver.find_element(*HomePage.partnerSelectElement).click()

	def selectClient(self):
		self.verifyElementPresence(HomePage.clientElement)
		self.driver.find_element(*HomePage.clientElement).click()
		self.driver.find_element(*HomePage.clientInputElement).send_keys(self.getData['client'])
		self.driver.find_element(*HomePage.clientSelectElement).click()

	def infrastructureTab(self):
		self.verifyElementPresence(HomePage.infrastructureTabElement)
		return self.driver.find_element(*HomePage.infrastructureTabElement)

	def logsLinkVisible(self):
		self.selectPartner()
		self.selectClient()
		self.infrastructureTab().click()
		self.driver.find_element(*HomePage.logsLinkElement).click()

