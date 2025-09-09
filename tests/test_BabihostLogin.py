import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,WebDriverException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.BabihostLogin import Babihost
from Utilities.utils import AutomationLogger




@pytest.mark.usefixtures("launchDriver")
class TestBabihostLogin:
    log = AutomationLogger.automation()
    test_data=AutomationLogger.get_newest_excel_file("C:\\Users\\User\\Babihost\\testData","Sheet1")
    @pytest.mark.parametrize("test_data",test_data)

    def test_login(self,test_data):

        try:
            self.log.info("Test started: test_login")
            babihost = Babihost(self.driver)
            babihost.BabihostLogin(**test_data)
            self.log.info("Login test completed successfully")   

            

        except Exception as e:
            self.log.error(f"An error occurred during login: {e}")
            pytest.fail(f"Test failed due to an exception: {e}")
            raise




   