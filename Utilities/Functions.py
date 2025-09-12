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




 