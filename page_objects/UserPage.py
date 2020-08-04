from .DefaultPage import DefaultPage
from ..locators.Common import Common


class UserPage(DefaultPage):

    def login_user(self, email, password):
        self._input(Common.user_login.email_input, email)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.submit)
        return self
    
    def login_admin(self, username, password):
        self._input(Common.user_login.username_input, username)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.submit)
        return self
    