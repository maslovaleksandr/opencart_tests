from .DefaultPage import DefaultPage
from .ProductPage import ProductPage
from .UserPage import UserPage
from ..locators import Main, Common

class MainPage(DefaultPage):

    def click_featured_products(self, number):
        number = number-1
        self._click(Main.featured.elements, index=number)
        return ProductPage(self.browser)

    def get_featured_products_text(self, number):
        index = number-1
        return self._get_text(Main.featured.names, index=index)

    def login_page(self):
        self._click(Common.user_login.my_account)
        self._click(Common.user_login.login_page)
        return UserPage(self.browser)

