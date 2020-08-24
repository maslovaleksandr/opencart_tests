from .DefaultPage import DefaultPage
from ..locators.Catalog import Catalog
from selenium.webdriver.support.ui import Select
from ..locators.Main import Main


class CatalogPage(DefaultPage):

    def open_phones_catalog(self):
        self._click(Main.main_menu.phones_and_pda)
        return self

    def sort_opened_catalog_by_name(self, param):
        """A_Z --- Z_A"""
        sort = self.select_from(Catalog.Sort.options)
        if param == "A_Z":
            sort.select_by_visible_text(Catalog.Sort.by_name_A_Z)
        elif param == "Z_A":
            sort.select_by_visible_text(Catalog.Sort.by_name_Z_A)
        else:
            raise("No such sort option")
        return self

    def sort_opened_catalog_by_price(self, param):
        """low_high --- high_low"""
        sort = self.select_from(Catalog.Sort.options)
        if param == "low_high":
            sort.select_by_visible_text(Catalog.Sort.by_price_low_high)
        elif param == "high_low":
            sort.select_by_visible_text(Catalog.Sort.by_price_high_low)
        else:
            raise("No such sort option")
        return self

    def sort_opened_catalog_by_model_name(self, param):
        """A_Z --- Z_A"""
        sort = self.select_from(Catalog.Sort.options)
        if param == "A_Z":
            sort.select_by_visible_text(Catalog.Sort.by_model_A_Z)
        elif param == "Z_A":
            sort.select_by_visible_text(Catalog.Sort.by_model_Z_A)
        else:
            raise("No such sort option")
        return self

    def change_view(self):
        if "active" in self._get_attr(Catalog.Navigation.grid_view, "class"):
            self._click(Catalog.Navigation.list_view)
        else:
            self._click(Catalog.Navigation.grid_view)
        return self
    
    def add_to_cart(self, index):
        self._click(Catalog.Buttons.add_to_cart_button, index)
        return self
    
    def add_wish_list(self, index):
        self._click(Catalog.Buttons.add_to_wish_list_button, index)
        return self
