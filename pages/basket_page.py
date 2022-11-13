from .base_page import BasePage
from .locators import BasketPageLocators
from .languages import Languages


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), "Basket not empty"

    def basket_empty_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text.split(" ")
        empty_basket_message = " ".join(empty_basket_message[:-2])
        assert empty_basket_message in Languages.empty_basket_messages.values(), "No message about empty basket"
