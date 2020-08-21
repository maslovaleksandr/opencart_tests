from .DefaultPage import DefaultPage
from .ProductPage import ProductPage
from .UserPage import UserPage
from ..locators import Main, Common



class MainPage(DefaultPage):

    def click_featured_products(self, number):
        self._click(Main.featured.elements, index=number)
        return ProductPage(self.browser)

    def get_featured_products_text(self, number):
        return self._get_text(Main.featured.names, index=number)

    def login_page(self):
        self._click(Common.user_login.my_account)
        self._click(Common.user_login.login_page)
        return UserPage(self.browser)

    def check_drop_down_menu(self):
        self.click_all_elements(Main.main_menu.elements)