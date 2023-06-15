import pytest
from selenium.common import NoSuchElementException, TimeoutException
from pageObjects.HamBurgerMenu import HamBurgerMenu
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=8)
@pytest.mark.usefixtures("getData")
class TestSaveViewFunctionality(BaseClass):

	def test_SaveViewFunctionality(self, getData):

		try:
			hamBurgerMenuPage = HamBurgerMenu(self.driver, getData)
			savedViewText = hamBurgerMenuPage.SavedViewList()
			savedViewDisplayStatus = self.isDisplayed(savedViewText)
			if not savedViewDisplayStatus:
				raise AssertionError("Saved View is not showing in View List")
		except(NoSuchElementException, TimeoutException):
			raise AssertionError("Logs View Functionality is not working ")

