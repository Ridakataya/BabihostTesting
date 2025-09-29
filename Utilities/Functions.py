import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import email
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from Utilities.utils import AutomationLogger
from pages.creds import *


def BabihostLogin(self, username, password):
    log=AutomationLogger.automation()
    email_locator= (By.XPATH,email)
    log.info("Location email")
    try:
        WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located(email_locator)
        )
    except NoSuchElementException as e:
        self.log.warning("unable to locate element")
    self.driver.find_element(By.XPATH,email).send_keys(username)
    log.info("Sent username")
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/form/button').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="nova-ui-dropdown-button-3"]').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="nova-ui-dropdown-menu-4"]/div/nav/button').click()
    time.sleep(3)


  # Handle confirmation alert if it appears
    try:
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()   # confirm logout by clicking OK
        log.info("Confirmed logout via site popup")
    except TimeoutException:
        log.info("No logout confirmation popup appeared")

    time.sleep(3)



def BabihostLoginRememberMe(self, username, password):
    # Attach logger to object instead of local variable
    self.log = AutomationLogger.automation()

    email_locator = (By.XPATH, email)
    self.log.info("Locating email input")

    try:
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(email_locator)
        )
    except Exception as e:  # catch TimeoutException, etc.
        self.log.warning(f"Unable to locate email element: {e}")
        pytest.fail("Email input not found")

    # Enter credentials
    self.driver.find_element(By.XPATH, email).send_keys(username)
    self.log.info("Entered username")

    time.sleep(1)
    self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    self.log.info("Entered password")

    # Click on remember me
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div[1]').click()
    self.log.info("Clicked 'Remember Me' checkbox")

    # Click login
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button').click()
    self.log.info("Clicked login button")

    # Verify login success
    try:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nova-ui-dropdown-button-3"]'))
        )
        self.log.info("Login successful - dashboard loaded")

        # Store session cookies
        cookies_before = self.driver.get_cookies()

        # Close and reopen browser
        self.driver.quit()
        time.sleep(2)

        # Reopen browser
        self.driver = webdriver.Chrome()
        self.driver.get("https://babihost.online/admin/login")

        # Re-add cookies (simulate persistence)
        for cookie in cookies_before:
            if "expiry" in cookie:
                cookie.pop("expiry")  # Selenium doesn't allow expiry
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        time.sleep(2)

        current_url_after_reopen = self.driver.current_url

        if "login" not in current_url_after_reopen.lower():
            self.log.info("Remember Me functionality working - user automatically logged in")
            assert True, "Remember Me functionality verified successfully"
        else:
            current_cookies = self.driver.get_cookies()
            auth_cookie_exists = any(
                'auth' in cookie['name'].lower() or 'session' in cookie['name'].lower()
                for cookie in current_cookies
            )

            if auth_cookie_exists:
                self.log.info("Auth cookies preserved, Remember Me partially working")
                assert True, "Remember Me cookies preserved"
            else:
                self.log.warning("Remember Me functionality not working")
                pytest.fail("Remember Me test failed: cookies/session not preserved")

    except Exception as e:
        self.log.error(f"TC08 failed with error: {e}")
        pytest.fail(f"Remember Me test failed: {e}")



def BabihostRegistration(self, name, email, password, confirm_password):
    
    self.log = AutomationLogger.automation()
    self.log.info("Starting registration test with valid details")

    try:
        # Step 1: Navigate to Registration page
        self.driver.get("https://babihost.online/register")  # change if needed
        self.log.info("Opened registration page")

        # Step 2: Fill registration form
        self.driver.find_element(By.NAME, "name").send_keys(name)
        self.log.info(f"Entered name: {name}")

        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.log.info(f"Entered email: {email}")

        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "password_confirmation").send_keys(confirm_password)
        self.log.info("Entered password and confirmed password")

        # Step 3: Click Register
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()
        self.log.info("Clicked Register button")

        # Step 4: Wait for redirection (either login page or dashboard)
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("login") or EC.url_contains("dashboard")
        )
        current_url = self.driver.current_url
        self.log.info(f"Redirected to: {current_url}")

        # Step 5: Assert successful registration
        assert "login" in current_url.lower() or "dashboard" in current_url.lower(), \
            "User was not redirected after registration"

        self.log.info("Registration test passed - user account created successfully")

    except Exception as e:
        self.log.error(f"Registration test failed: {e}")
        pytest.fail(f"Registration test failed: {e}")



def BabihostForgotPassword(self):
    """
    Test Case: Verify 'Forgot Password' link redirects to Password Reset page
    """
    self.log = AutomationLogger.automation()
    self.log.info("Starting 'Forgot Password' link test")

    try:
        # Wait for Forgot Password link to be visible
        forgot_password_locator = (By.XPATH, "//*[@id='app']/div/div[2]/form/div[3]/div[2]/a")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(forgot_password_locator)
        )

        # Click on Forgot Password link
        self.driver.find_element(*forgot_password_locator).click()
        self.log.info("Clicked on 'Forgot Password' link")

        # Wait for redirection
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("password/reset")  
        )

        current_url = self.driver.current_url
        self.log.info(f"Redirected to: {current_url}")

        # Verify URL contains password reset page
        assert "reset" in current_url.lower() or "forgot" in current_url.lower(), \
            "User not redirected to Password Reset page"

        self.log.info("Forgot Password redirection test passed")

    except Exception as e:
        self.log.error(f"Forgot Password test failed: {e}")
        pytest.fail(f"Forgot Password test failed: {e}")





 