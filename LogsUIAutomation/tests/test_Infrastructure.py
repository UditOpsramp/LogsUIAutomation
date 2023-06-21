import pytest
from selenium.common import TimeoutException

from pageObjects import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.run(order=2)
@pytest.mark.usefixtures("getData")
class TestInfrastructureTabVisible(BaseClass):

    def test_InfrastructureTabVisible(self, getData):

        homepage = HomePage.HomePage(self.driver, getData)

        try:
            homepage.infrastructureTab()
        except TimeoutException:
            raise AssertionError("InfrastructureTab is not visible on Home Page")
