from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_product_to_the_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "ERROR: basket button is not presented"

    def add_product_to_the_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        # self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"

    def added_product_should_be_actual(self):
        """Метод, который проверяет, совпадает ли добавленная книга с текущей."""
        current_product = self.browser.find_element(*ProductPageLocators.CURRENT_PRODUCT).text
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        assert current_product == added_product, "ERROR: current and added product doesnt match"

    def prices_should_be_actual(self):
        """Метод, который проверяет, совпадает ли цена книги с общей ценой в корзине"""
        current_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).text
        assert current_price == basket_amount, "ERROR: current price and basket amount doesnt match"
