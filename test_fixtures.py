"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selene import browser

def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]} x {screen_size[1]}"


@pytest.fixture(params=[(1920, 1080), (1366, 768)], ids=show_screen_size)
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(1024, 1366), (430, 932)], ids=show_screen_size)
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
