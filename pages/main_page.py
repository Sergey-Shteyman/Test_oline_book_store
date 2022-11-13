from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def see_the_sore_view(self):
        store_view_button = self.browser.find_element(*MainPageLocators.STORE_VIEW)
        store_view_button.click()

    def go_to_all_product_page(self):
        all_products_button = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS)
        all_products_button.click()
