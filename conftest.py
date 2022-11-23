import webbrowser

import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_open():
    b = browser.open('https://google.com')
    print("Браузер открыт")
    return b
@pytest.fixture()
def browser_closed():
    print("Браузер закрыт")

@pytest.fixture(scope="session")
def max_res():
    width = browser.config.window_width = 1000
    height = browser.config.window_height = 500
    return width, height