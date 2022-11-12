from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self._should_be_login_url()
        self._should_be_login_form()
        self._should_be_register_form()

    def _should_be_login_url(self):
        assert "login" in self.browser.current_url, 'LoginError: Can not find "login" in current url'

    def _should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def _should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
