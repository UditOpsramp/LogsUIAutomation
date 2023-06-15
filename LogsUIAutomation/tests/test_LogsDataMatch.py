import time

import pytest
from selenium.common import TimeoutException

from generateLogs import logsGenerator
from pageObjects.Login_Page import LoginPage
from pageObjects.LogsPage import LogsPage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=5)
@pytest.mark.usefixtures("getLogCountData", "getData")
class TestLogsDataMatch(BaseClass):

	def test_logsDataMatch(self, getLogCountData, getData):

		PostedLog = logsGenerator.LogsGenerator(getLogCountData)
		logsPage = LogsPage(self.driver, getData)

		try:
			logsMessage = logsPage.getLogsMessageText()
		except TimeoutException:
			logsMessage = ''

		assert logsMessage == PostedLog, "UI Logs Message is not similar with Posted Log Message"
