import pytest
from selenium.common import TimeoutException, NoSuchElementException

from pageObjects.Login_Page import LoginPage
from generateLogs import logsGenerator
from pageObjects.LogsPage import LogsPage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=6)
@pytest.mark.usefixtures("getLogCountData", "getData")
class TestFilterSelection(BaseClass):

	def test_FilterSelectionFunctionality(self, getLogCountData, getData):

		logsGenerator.LogsGenerator(getLogCountData)
		logsPage = LogsPage(self.driver, getData)

		try:
			label_Value, operator_Value, value_Value = logsPage.clickedFilterSelection()

			if label_Value != "level":
				raise AssertionError("Label is not selected the clicked-one")
			elif operator_Value != "=":
				raise AssertionError("Operator is not selected the clicked-one")
			elif value_Value != "Debug":
				raise AssertionError("Value is not selected the clicked-one")

		except (TimeoutException, NoSuchElementException):
			raise AssertionError("Log Query Filter is not working properly")
