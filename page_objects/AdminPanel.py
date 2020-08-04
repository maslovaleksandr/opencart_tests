from .DefaultPage import DefaultPage
from ..locators import Admin
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class AdminPanel(DefaultPage):

    def go_to_downloads(self):
        self._click(Admin.catalog, 1)
        self._click(Admin.downloads, 1)
        return self

    def add_new_image(self):
        path_dir = os.path.dirname(__file__)
        file_path = os.path.join(path_dir, "../test_upload/sel.png")
        self._click(Admin.plus_button, 1)
        self.browser.execute_script(open("./upload.js").read())
        self._click(Admin.upload_button, 1)
        ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)
        self._input(Admin.input_file, file_path)
