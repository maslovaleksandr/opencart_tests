from ..page_objects.MainPage import MainPage


def test_click_featured(browser):
    MainPage(browser).click_featured_products(1)

def test_back_to_main_page(browser):
    product = MainPage(browser).click_featured_products(1)
    product.back_to_main_page()

def test_drop_down_menu(browser):
    MainPage(browser).check_drop_down_menu()

