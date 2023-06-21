from selenium.webdriver.common.by import By

from pageObjects.LogsPage import LogsPage
from utilities.BaseClass import BaseClass


class HamBurgerMenu(BaseClass):

	def __init__(self, driver, getData):
		self.driver = driver
		self.getData = getData

		logsPage = LogsPage(self.driver, self.getData)

		logsPage.addFilter()

	hamBurgerButton = (By.XPATH, "//button/span[@class='icon-navigation']")
	addViewButton = (By.XPATH, "//button[@title='Add Current View']/span[@class='icon-add']")
	viewNameTextBoxElement = (By.XPATH, "//form/div[1]/div[2]/input")
	viewAddButtonElement = (By.XPATH, "//form/div[3]/button[text()='add']")
	savedViewsElement = (By.XPATH, "//div/ul[@role='listbox']/li/span[@title='LogsUIAutomationView']")
	deleteViewElement = (By.XPATH, "//div/ul[@role='listbox']/li/button[2]/span")

	def HamBurgerMenu(self):
		self.verifyElementPresence(HamBurgerMenu.hamBurgerButton)
		self.driver.find_element(*HamBurgerMenu.hamBurgerButton).click()

	def AddViewButton(self):
		self.HamBurgerMenu()
		self.verifyElementPresence(HamBurgerMenu.addViewButton)
		self.driver.find_element(*HamBurgerMenu.addViewButton).click()
		self.driver.find_element(*HamBurgerMenu.viewNameTextBoxElement).send_keys("LogsUIAutomationView")
		self.driver.find_element(*HamBurgerMenu.viewAddButtonElement).click()

	def SavedView(self):
		self.AddViewButton()
		self.verifyElementPresence(HamBurgerMenu.savedViewsElement)
		return self.driver.find_element(*HamBurgerMenu.savedViewsElement)
