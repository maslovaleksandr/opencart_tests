from ..page_objects import UserPage, AdminPanel


def test_login_admin(browser):
    UserPage(browser).login_admin("user", "user")
    AdminPanel(browser)\
        .go_to_downloads()\
        .add_new_image()
        