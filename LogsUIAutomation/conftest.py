import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from TestData import LoginData, LogGeneratorCount


@pytest.fixture(scope="class")
def setup(request):
	# service_obj = Service("/home/udit/Documents/LogsUIAutomation/geckodriver")
	# driver = webdriver.Firefox(service=service_obj)
	capabilities = {
		"browserName": "firefox",
		"browserVersion": "96.0",
		"selenoid:options": {
			"enableVNC": True,
			"enableVideo": False
		}
	}
	driver = webdriver.Remote(
		command_executor='http://172.26.1.88:4444/wd/hub',
		desired_capabilities=capabilities)

	driver.maximize_window()
	request.cls.driver = driver
	yield
	driver.quit()


@pytest.fixture(scope="class", params=LoginData.LoginData.test_login_data)
def getData(request):
	return request.param


@pytest.fixture(scope="class", params=LogGeneratorCount.LogGeneratorCount.test_login_data)
def getLogCountData(request):
	return request.param
