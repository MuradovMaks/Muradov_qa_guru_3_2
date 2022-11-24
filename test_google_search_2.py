import pytest
from selene.support.shared import browser
from selene import be, have

def test_search_text(browser_open):
    browser.element('[name="q"]').should(be.blank).type('Selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search_text_negative(browser_open):
    browser.element('[name=q]').should(be.blank).type("zgfdgdsgsg").press_enter()
    browser.element('[id=search]').should(have.text('abrakadabra'))
