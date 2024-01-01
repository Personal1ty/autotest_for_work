from .pages.register_page_bilbet import RegisterPageBilbet


def test_guest_can_do_register(browser):
    link = "https://preprodappbets.dimatech.org/"
    page = RegisterPageBilbet(browser, link)
    page.open()
    page.clicked_register_button()
    page.check_select_currency_register_popup()
    page.check_welcome_bonus_inr_register_popup()
    page.check_correct_email_and_pass_register_popup()
    page.input_registration_credentials_register_popup()