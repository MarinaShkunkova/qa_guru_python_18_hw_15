"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]} x {screen_size[1]}"


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1024, 1366), (430, 932)], ids=show_screen_size)
def browser_settings(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize("browser_settings", [(1920, 1080), (1600, 900)], indirect=True, ids=show_screen_size)
def test_github_desktop(browser_settings):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


@pytest.mark.parametrize("browser_settings", [(1024, 1366), (430, 932)], indirect=True, ids=show_screen_size)
def test_github_mobile(browser_settings):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
