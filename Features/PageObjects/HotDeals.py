from selenium.webdriver.common.by import By

from Features.PageObjects.TopNav.NavigationMenu import NavigationMenu


class HotDeals(NavigationMenu):
    def __init__(self, driver):
        super().__init__(driver)


    def accept_cookies(self):
        self.driver.find_element(By.ID, 'privacy_pref_optin').click()
        self.driver.find_element(By.CSS_SELECTOR, '.sign-in-btn').click()


