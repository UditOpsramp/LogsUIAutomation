from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class LogsPage(BaseClass):
	logsExplorerPageTextElement = (By.XPATH, "//div[@data-type='Pane']/div/div[2]/div/p[1]")
	logsMessageElement = (By.XPATH, "//div[@ref='eCenterContainer']/div/div[@col-id='message']")
	addFilterElement = (By.XPATH, "//div[@data-testid='logs-query-builder']")

	AddFilter_Label = 'level'
	AddFilter_Operator = 'Equals'
	AddFilter_Value = 'Debug'

	selectAddFilter_LabelElement = (By.XPATH, "//div[@role='listbox']/ul/li/span[text()=" + "'" + AddFilter_Label + "']")
	selectAddFilter_OperatorElement = (By.XPATH, "//div[@role='listbox']/ul/li/span/span[text()=" + "'" + AddFilter_Operator + "']")
	selectAddFilter_ValueElement = (By.XPATH, "//div[@role='listbox']/ul/li/span[text()=" + "'" + AddFilter_Value + "']")

	def __init__(self, driver, getData):
		self.driver = driver
		self.getData = getData

		homePage = HomePage(self.driver, self.getData)
		homePage.logsLinkVisible()

	def getLogsExplorerPageText(self):
		self.verifyElementPresence(LogsPage.logsExplorerPageTextElement)
		return self.driver.find_element(*LogsPage.logsExplorerPageTextElement).text

	def getLogsMessageText(self):
		self.verifyElementPresence(LogsPage.logsMessageElement)
		return self.driver.find_element(*LogsPage.logsMessageElement).text

	def addFilterButtonClick(self):
		self.verifyElementPresence(LogsPage.addFilterElement)
		self.driver.find_element(*LogsPage.addFilterElement).click()

	def selectLabel_AddFilter(self):
		self.verifyElementPresence(LogsPage.selectAddFilter_LabelElement)
		self.driver.find_element(*LogsPage.selectAddFilter_LabelElement).click()

	def selectOperator_AddFilter(self):
		self.driver.find_element(*LogsPage.selectAddFilter_OperatorElement).click()

	def selectValue_AddFilter(self):
		self.driver.find_element(*LogsPage.selectAddFilter_ValueElement).click()

	def addFilter(self):
		self.addFilterButtonClick()
		self.selectLabel_AddFilter()
		self.selectOperator_AddFilter()
		self.selectValue_AddFilter()

	def clickedFilterSelection(self):
		self.addFilter()
		label_Value = self.driver.find_element(By.XPATH, "//button[@data-segment-type='key']").text
		operator_Value = self.driver.find_element(By.XPATH, "//button[@data-segment-type='operator']").text
		value_Value = self.driver.find_element(By.XPATH, "//button[@data-segment-type='value']").text
		return label_Value, operator_Value, value_Value

	def queryFilterFunctionality(self):
		self.addFilter()
		self.driver.find_element(By.XPATH, "//canvas[@data-zr-dom-id='zr_0']").click()
		return self.driver.find_element(By.XPATH, "//div[@class='echarts-for-react h-full']/div[2]/div/div[2]/span[3]").text

