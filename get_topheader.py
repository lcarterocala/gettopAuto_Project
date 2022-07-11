from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class Header(Page):

    # locators
    SEARCH_INPUT = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
    SEARCH_ICON = (By.CSS_SELECTOR, 'a.is-small i.icon-search')
    SEARCH_BTN = (By.CSS_SELECTOR, 'div.flex-col button.submit-button')

    def search_icon_hover(self):
        actions = ActionChains(self.driver)
        search_icon = self.find_element(*self.SEARCH_ICON)
        actions.move_to_element(search_icon)
        actions.perform()
        sleep(7)

    def search_gettop(self, search_word):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_word)

    def search_button_click(self):
        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        # search_btn = self.driver.find_element(*self.SEARCH_BTN)
        # self.click(search_btn)
        search_btn.click()
