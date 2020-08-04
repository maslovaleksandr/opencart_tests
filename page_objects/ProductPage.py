from ..locators import Product
from .DefaultPage import DefaultPage


class ProductPage(DefaultPage):

    def add_to_wish_list(self):
        self._click(Product.wish_list)
        return self

    def add_to_cart(self):
        self._click(Product.add_to_cart)
        return self

    def add_to_compare(self):
        self._click(Product.compare)
        return self
