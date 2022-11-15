import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.all_products_page import AllProductsPage


@pytest.mark.xfail(reason="must fall")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.see_the_sore_view()
    main_page.go_to_all_product_page()
    all_products_page = AllProductsPage(browser, browser.current_url)
    all_products_page.go_to_products_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_the_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.see_the_sore_view()
    main_page.go_to_all_product_page()
    all_products_page = AllProductsPage(browser, browser.current_url)
    all_products_page.go_to_products_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="must fall")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.see_the_sore_view()
    main_page.go_to_all_product_page()
    all_products_page = AllProductsPage(browser, browser.current_url)
    all_products_page.go_to_products_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_the_basket()
    product_page.success_message_is_disappeared()
