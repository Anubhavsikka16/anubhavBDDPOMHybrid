import webbrowser

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.firefox.options import Options

from Utilities import ConfigReader
import sys

print(sys.path)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call): # item is call to test item and call is call to the test containing all info on test
    outcome = yield #It allows the test to run and the function to "pause" until the test is finished. This means that the test function runs as usual, and the hook can inspect its result afterward.
    rep = outcome.get_result()
    #After the yield, outcome.get_result() retrieves the result of the test execution. This is the outcome report for the test (e.g., passed, failed, skipped, etc.).
    print("result of the test is: ", rep)
    setattr(item, "rep_" + rep.when, rep) #This line adds the result (report) to the test item (item) as an attribute.
    return rep


@pytest.fixture()
# Fixture to log failure details and capture a screenshot if a test fails.
def log_on_failure(request, get_browser):
    yield
    item = request.node  # Access the current test item (function or parameterized instance).
    print("Name of the test running is: ", item.name)
    '''
    You can use request.node to access various details, such as:

    Test Name: request.node.name will give you the name of the current test.

    Test ID: request.node.nodeid provides a unique identifier for the test.

    Test Object: You can use request.node to access attributes like the test's arguments, markers, etc.
    '''

    driver = get_browser  # Access the WebDriver instance.
    if item.rep_call.failed:  # Check if the test execution resulted in failure.
        # Capture a screenshot and attach it to the Allure report.
        allure.attach(driver.get_screenshot_as_png(), name="Bablic_login", attachment_type=AttachmentType.PNG)


@pytest.fixture( params=["firefox", "edge"], scope="function")
def get_browser(request):
    global driver
    if ConfigReader.read_config("env_info","env") == "remote":
        remote_url = "http://localhost:4444/wd/hub" 
        if request.param == "chrome":
            chrome_options = webdriver.ChromeOptions()
            driver=webdriver.Remote(command_executor=remote_url, options=chrome_options)
        elif request.param == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = False
            driver=webdriver.Remote(command_executor=remote_url, options=firefox_options)
        elif request.param == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.headless = False
            driver=webdriver.Remote(command_executor=remote_url, options=edge_options)
        else:
            print("No browser found to run tests")
            
        request.cls.driver = driver
        driver.get(ConfigReader.read_config("env_info", "test_url"))

        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    elif ConfigReader.read_config("env_info","env")=="localhost":
        if ConfigReader.read_config("env_info","browser") == "chrome":
            driver = webdriver.Chrome()
        elif ConfigReader.read_config("env_info","browser") == "firefox":
            driver = webdriver.Firefox()
        request.cls.driver = driver
        driver.get(ConfigReader.read_config("env_info","test_url"))
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
