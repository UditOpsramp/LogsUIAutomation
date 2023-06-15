import pytest
from selenium.common import TimeoutException, NoSuchElementException

from generateLogs import logsGenerator
from pageObjects.LogsPage import LogsPage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=7)
@pytest.mark.usefixtures("getLogCountData", "getData")
class TestAddFilter(BaseClass):

	def test_AddFilterFunctionality(self, getLogCountData, getData):

		logsGenerator.LogsGenerator(getLogCountData)
		logsPage = LogsPage(self.driver, getData)

		try:
			addFilterValue = logsPage.queryFilterFunctionality()
			if addFilterValue != logsPage.AddFilter_Value:
				raise AssertionError("Filter Functionality is not working Properly")
		except (TimeoutException, NoSuchElementException):
			raise AssertionError("Log Query Filter is not working properly")

