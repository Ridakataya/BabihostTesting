import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,WebDriverException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from Utilities.utils import AutomationLogger
from pages.BabihostRegistration import Registration

@pytest.mark.usefixtures("launchDriver")
class TestBabihostRegistration:
    log = AutomationLogger.automation()
    test_data=AutomationLogger.get_newest_excel_file("testData","Sheet3")
    @pytest.mark.parametrize("test_data",test_data)

    def test_registration(self,test_data):

        try:
            self.log.info("Test started: test_registration")
            babihost = Registration(self.driver)
            babihost.BabihostRegistration(**test_data)
            self.log.info("Registration test completed successfully")   

            

        except Exception as e:
            self.log.error(f"An error occurred during registration: {e}")
            pytest.fail(f"Test failed due to an exception: {e}")
            raise