import pytest
from selene.support.shared import browser




@pytest.fixture(scope="session")
def browser_max():
    browser.config.window_height = 960
    browser.config.window_width = 720
    browser.open('https://google.com')


@pytest.fixture(scope="function")
def clear_field():
    yield
    browser.element('[name="q"]').clear()