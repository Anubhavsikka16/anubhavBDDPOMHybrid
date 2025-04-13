
from selenium.common.exceptions import NoSuchElementException

from Utilities import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, selector, locator_value):
        """
        Check if an element is present on the page.
        """
        try:
            self.driver.find_element(by=selector, value=ConfigReader.read_config('locators', locator_value))
            return True
        except NoSuchElementException:
            return False

    def click(elf, locator):
        if str(locator).endswith('_XPATH'):
            ConfigReader.read_config('locators', locator).click()
        elif str(locator).endswith('_CSS'):
            ConfigReader.read_config('locators', locator).click()
        elif str(locator).endswith('_ID'):
            ConfigReader.read_config('locators', locator).click()

    def send_keys(self, locator, value):
        if str(locator).endswith('_XPATH'):
            ConfigReader.read_config('locators', locator).send_keys(value)
        elif str(locator).endswith('_CSS'):
            ConfigReader.read_config('locators', locator).send_keys(value)
        elif str(locator).endswith('_ID'):
            ConfigReader.read_config('locators', locator).send_keys(value)

    def get_text(self, locator):
        if str(locator).endswith('_XPATH'):
            return ConfigReader.read_config('locators', locator).text
        elif str(locator).endswith('_CSS'):
            return ConfigReader.read_config('locators', locator).text
        elif str(locator).endswith('_ID'):
            return ConfigReader.read_config('locators', locator).text

    def get_attribute(self, locator, attribute):
        if str(locator).endswith('_XPATH'):
            return ConfigReader.read_config('locators', locator).get_attribute(attribute)
        elif str(locator).endswith('_CSS'):
            return ConfigReader.read_config('locators', locator).get_attribute(attribute)
        elif str(locator).endswith('_ID'):
            return ConfigReader.read_config('locators', locator).get_attribute(attribute)

    def move_to_element(self, locator):
        global element
        if str(locator).endswith('_XPATH'):
            element = ConfigReader.read_config('locators', locator)
        elif str(locator).endswith('_CSS'):
            element = ConfigReader.read_config('locators', locator)
        elif str(locator).endswith('_ID'):
            element = ConfigReader.read_config('locators', locator)

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()