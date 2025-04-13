from selenium.webdriver.common.by import By

from Features.PageObjects.BasePage import BasePage
from Features.PageObjects.HotDeals import HotDeals
from Features.PageObjects.TopNav.NavigationMenu import NavigationMenu


class Homepage(NavigationMenu):
    def __init__(self, driver):
        super().__init__(driver)

    def navigation_check(self):
        NavigationMenu.total_anchor_tags(self)
        self.driver.find_element(By.CSS_SELECTOR, ".megamenu-list>a[href='/hot-deals/']").click()

        return HotDeals(self.driver)

