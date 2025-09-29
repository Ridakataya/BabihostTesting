import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.utils import AutomationLogger
from pages.Forgotpassword import Forgotpassword


@pytest.mark.usefixtures("launchDriver")
class TestBabihostForgotpassword:
    log = AutomationLogger.automation()

    def test_forgot_password_link(self):
        """
        Verify 'Forgot Password' link redirects user to Reset Password page
        """
        try:
            self.log.info("Test started: test_forgot_password_link")
            forgot_password_page = Forgotpassword(self.driver)

            # Call the function (no email needed)
            forgot_password_page.BabihostForgotPassword()

            # Final assertion for extra safety
            assert "reset" in self.driver.current_url.lower(), \
                "User was not redirected to Reset Password page"

            self.log.info("Forgot Password test completed successfully")

        except TimeoutException:
            self.log.error("Reset Password page did not load in time")
            pytest.fail("Reset Password page did not load in time")

        except Exception as e:
            self.log.error(f"An error occurred during Forgot Password test: {e}")
            pytest.fail(f"Test failed due to an exception: {e}")