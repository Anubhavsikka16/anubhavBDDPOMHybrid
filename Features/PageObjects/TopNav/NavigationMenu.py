from selenium.webdriver.common.by import By
from selenium import webdriver


import requests

from Features.PageObjects.BasePage import BasePage


class NavigationMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def total_anchor_tags(self):


        nav_menu = self.driver.find_element(By.CSS_SELECTOR, 'ul[class$=\'megamenu\']')
        list_anchor_tags = nav_menu.find_elements(By.TAG_NAME, 'a')

        for anchor_tag in list_anchor_tags:
            hrefs = anchor_tag.get_attribute('href')
            for href in hrefs:
                print(href)
                break

            if requests.head(hrefs).status_code == 200:
                print(f"Valid link: {hrefs}")
            else:
                print(f"Invalid link: {hrefs}")






