from ..locators import Common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UserLogin:
    def __init__(self, browser):
        self.browser = browser

    def click_login(self):
        WebDriverWait(self.browser, 20)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, Common.user_login.my_account['css'])))\
                .click()
        WebDriverWait(self.browser, 20)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, Common.user_login.login_page['css'])))\
                .click()


