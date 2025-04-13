
import allure

import sys

print("Python Path:", sys.path)


from selenium import webdriver

from Utilities import ConfigReader



def before_scenario(context, scenario):



    if ConfigReader.read_config('env_info', 'browser') == 'chrome':
        context.driver=webdriver.Chrome()
    elif ConfigReader.read_config('env_info', 'browser') == 'firefox':
        context.driver=webdriver.Firefox()


    context.driver.get("https://www.greenmangaming.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def before_step(context, step):
    """
    This function is executed before each step.
    It can be used to set up any preconditions for the step.
    """
    if step.status=='failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        allure.attach(context.driver.get_screenshot_as_png(), name='error', attachment_type=allure.attachment_type.PNG)

