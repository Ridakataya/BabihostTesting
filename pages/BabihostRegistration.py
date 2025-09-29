import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *


class Registration():
    def __init__(self,driver):
        self.driver = driver
        self.log = AutomationLogger.automation()

    def BabihostRegistration(self,name,email,password,confirm_password):  #page of babihost registration
        BabihostRegistration(self,name,email,password,confirm_password)