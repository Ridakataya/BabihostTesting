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
    WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="nova-ui-dropdown-button-3"]'))
    )
    dropdown_button = self.driver.find_element(By.XPATH, '//*[@id="nova-ui-dropdown-button-3"]')

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