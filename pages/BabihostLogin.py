import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *


class Babihost():
    def __init__(self,driver):
        self.driver = driver

    def BabihostLogin(self,username,password):  #page of babihost login
        BabihostLogin(self,username,password)
