import pytest
from selenium.common import TimeoutException, NoSuchElementException

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=3)
@pytest.mark.usefixtures("getData")
class TestLogsLinkVisible(BaseClass):

	def test_LogsLinkVisible(self, getData):
		homepage = HomePage(self.driver, getData)

		try:
			homepage.logsLinkVisible()
		except (TimeoutException, NoSuchElementException):
			raise AssertionError("Logs Link is not visible under Infrastructure Tab")
