#rapatative 
#Login Structure
#browsers I'm using
#screen shots on failure tests
#report edits

import pytest
from selenium import webdriver
import os


@pytest.fixture(scope="class") #scope class, runs before any class test
def launchDriver(request):
    driver = webdriver.Chrome()
    driver.get("https://babihost.online/admin/login")
    request.cls.driver = driver
    yield #run the tests,then continue
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Default test name
    test_item = item.name

    # If test is parametrized (contains '[' in nodeid), extract the parameter
    if "[" in item.nodeid:
        try:
            test_item = item.nodeid.split("[")[1].split("]")[0].split("-")[-1].strip()
        except Exception:
            test_item = item.name  # fallback to test name

    # You can now log/save test_item without crashing
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Example: log test status
        print(f"Test '{test_item}' result: {report.outcome}")


def pytest_html_report_title(report):
    report.title = 'QA Automation Test'







        
