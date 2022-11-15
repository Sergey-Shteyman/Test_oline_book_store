from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def see_the_sore_view(self):
        store_view_button = self.browser.find_element(*MainPageLocators.STORE_VIEW)
        store_view_button.click()

    def go_to_all_product_page(self):
        all_products_button = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS)
        all_products_button.click()
