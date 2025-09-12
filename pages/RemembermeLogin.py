import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *

class Rememberme():
    def __init__(self,driver):
        self.driver = driver
        self.log = AutomationLogger.automation()

    def BabihostLoginRememberMe(self,username,password):  #page of babihost login with remember me option
        BabihostLoginRememberMe(self,username,password)