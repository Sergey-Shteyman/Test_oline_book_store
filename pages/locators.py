from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a#login_link")
    STORE_VIEW = (By.CSS_SELECTOR, "a.dropdown-toggle")
    ALL_PRODUCTS = (By.XPATH, '//ul[@class="dropdown-menu"]/li[1]/a[1]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT = (By.CSS_SELECTOR, "a#logout_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    EMAIL_LABEL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD_LABEL = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REPEAT_PASSWORD_LABEL = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    CURRENT_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "div#messages :nth-child(1) :nth-child(2) > strong")
    BASKET_AMOUNT = (By.CSS_SELECTOR, "div#messages :nth-child(3) > .alertinner > p > strong")
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[1]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages :nth-child(1) :nth-child(2)")


class AllProductsPageLocators:
    SHELL_CODERS_BOOK = (By.CSS_SELECTOR, "div.image_container :nth-child(1) > img.thumbnail")


class BasketPageLocators:
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "div#content_inner > p > a")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")
