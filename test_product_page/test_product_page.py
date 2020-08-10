from ..page_objects import MainPage, ProductPage
import time

def test_add_product_to_cart(browser):
    MainPage(browser)\
        .click_featured_products(1)\
        .add_to_cart()
    time.sleep(2)


def test_add_product_to_wish_list(browser):
    MainPage(browser).click_featured_products(2)
    ProductPage(browser).add_to_wish_list().add_to_compare()



