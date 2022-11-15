from .base_page import BasePage
from .locators import AllProductsPageLocators


class AllProductsPage(BasePage):

    def go_to_products_page(self):
        shell_coders_book = self.browser.find_element(*AllProductsPageLocators.SHELL_CODERS_BOOK)
        shell_coders_book.click()
