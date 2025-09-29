import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *

class Forgotpassword():
    def __init__(self,driver):
        self.driver = driver
        self.log = AutomationLogger.automation()

    def BabihostForgotPassword(self):  #page of babihost forgot password
        BabihostForgotPassword(self)