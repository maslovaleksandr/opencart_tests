from ..page_objects import MainPage, UserPage


def test_login(browser):
    MainPage(browser).login.click_login()
    UserPage(browser).login_user("test@test.test", "test").make_screenshot(filename= __file__ + ".png")
    
