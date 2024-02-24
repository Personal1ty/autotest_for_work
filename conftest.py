import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                     help="Choose language")

@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    # Resize the window to the screen width/height
    browser.set_window_size(360, 800)
    # Move the window to position x/y
    #browser.set_window_position(200, 200)
    yield browser
    print("\nquit browser..")