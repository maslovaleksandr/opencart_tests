from ..page_objects import MainPage
import time

def test_add_product_to_wish_list(browser):
    MainPage(browser)\
        .click_featured_products(1)\
        .add_to_wish_list()\
        .add_to_compare()


def test_add_product_to_cart(browser):
    MainPage(browser)\
        .click_featured_products(1)\
        .add_to_cart()
    time.sleep(2)
