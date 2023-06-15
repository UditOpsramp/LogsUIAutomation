import pytest
from selenium.common import TimeoutException, NoSuchElementException

from pageObjects.Login_Page import LoginPage
from utilities.BaseClass import BaseClass

loginStatus = True


@pytest.mark.run(order=1)
@pytest.mark.usefixtures("getData")
class TestLogin(BaseClass):

	def test_Login(self, getData):

		global loginStatus
		loginPage = LoginPage(self.driver, getData)
		loginPage.loginSubmit()

		try:
			loginErrorElement = loginPage.loginError()
			incorrectCredsStatus = self.isDisplayed(loginErrorElement)
		except NoSuchElementException:
			incorrectCredsStatus = False

		if not incorrectCredsStatus:
			try:
				loginSuccessElement = loginPage.loginSuccess()
				loginStatus = self.isDisplayed(loginSuccessElement)
			except (NoSuchElementException, TimeoutException):
				loginStatus = False

		if incorrectCredsStatus:
			raise AssertionError("You are giving wrong credentials")
		elif not loginStatus:
			raise AssertionError("Login Failed")
