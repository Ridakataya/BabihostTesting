import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,WebDriverException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from Utilities.utils import AutomationLogger
from pages.RemembermeLogin import Rememberme

@pytest.mark.usefixtures("launchDriver")
class TestRemembermeLogin:
    log = AutomationLogger.automation()
    test_data=AutomationLogger.get_newest_excel_file("testData","Sheet2")
    @pytest.mark.parametrize("test_data",test_data)

    def test_login_rememberme(self,test_data):
        
        try:
            self.log.info("Test started: test_login_rememberme")
            babihost = Rememberme(self.driver)
            babihost.BabihostLoginRememberMe(**test_data)
            self.log.info("Remember Me login test completed successfully")


        except Exception as e:
            self.log.error(f"An error occurred during Remember Me login: {e}")
            pytest.fail(f"Test failed due to an exception: {e}")
            raise