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

    def register_new_user(self, email, password):
        email_label = self.browser.find_element(*LoginPageLocators.EMAIL_LABEL)
        email_label.send_keys(email)
        password_label = self.browser.find_element(*LoginPageLocators.PASSWORD_LABEL)
        password_label.send_keys(password)
        repeat_password_label = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_LABEL)
        repeat_password_label.send_keys(password)
        registration_submit_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_submit_btn.click()
