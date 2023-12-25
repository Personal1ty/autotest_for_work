from .pages.register_page_bilbet import RegisterPageBilbet


def test_guest_can_do_register(browser):
    link = "https://preprodappbets.dimatech.org/"
    page = RegisterPageBilbet(browser, link)
    page.open()
    page.clicked_register_page()
    page.check_select_currency()
    page.check_welcome_bonus()