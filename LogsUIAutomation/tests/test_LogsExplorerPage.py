import pytest
from selenium.common import NoSuchElementException, TimeoutException

from pageObjects.LogsPage import LogsPage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=4)
@pytest.mark.usefixtures("getData")
class TestLogsExplorerPage(BaseClass):

	def test_LogsExplorerPage(self, getData):

		try:
			logsPage = LogsPage(self.driver, getData)
			logsPage.getLogsExplorerPageText()
		except(NoSuchElementException, TimeoutException):
			raise AssertionError("Logs Explorer Page is not loading fine")
