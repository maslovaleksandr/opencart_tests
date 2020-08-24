from ..page_objects.CatalogPage import CatalogPage
import time
import random

def test_sort(browser):
    CatalogPage(browser)\
        .open_phones_catalog()\
        .sort_opened_catalog_by_name("Z_A")\
        .make_screenshot("sorted.png")
    time.sleep(3)


def test_view(browser):
    CatalogPage(browser)\
        .open_phones_catalog()\
        .change_view()
    time.sleep(2)
    CatalogPage(browser).change_view()
    time.sleep(2)

 
def test_adding_to_cart(browser):
    CatalogPage(browser)\
        .open_phones_catalog()\
        .add_to_cart(random.randint(0,3))\
        .change_view()\
        .add_wish_list(random.randint(0,3))
    time.sleep(5)
