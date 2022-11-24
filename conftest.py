import webbrowser

import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    width = browser.config.window_width = 1000
    height = browser.config.window_height = 500
    b = browser.open('https://google.com')
    print("Браузер открыт")
    yield width, height, b
    print("Браузер закрыт")

