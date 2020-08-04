from ..locators import Common


class UserLogin:
    def __init__(self, browser):
        self.browser = browser

    def click_login(self):
        self.browser.find_element_by_css_selector(Common.user_login.my_account['css']).click()
        self.browser.find_element_by_css_selector(Common.user_login.login_page['css']).click()


