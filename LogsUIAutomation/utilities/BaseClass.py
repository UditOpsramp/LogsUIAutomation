import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

	def isDisplayed(self, element):
		return element.is_displayed()

	def verifyElementPresence(self, element):
		WebDriverWait(self.driver, 30).until((expected_conditions.presence_of_element_located(element)))

