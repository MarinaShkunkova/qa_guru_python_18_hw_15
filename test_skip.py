"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
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
    if width > 1024:
        yield "desktop"
    else:
        yield "mobile"
    browser.quit()


def test_github_desktop(browser_settings):
    if browser_settings == "mobile":
        pytest.skip("Мобильное соотношение сторон")
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()


def test_github_mobile(browser_settings):
    if browser_settings == "desktop":
        pytest.skip("Десктопное соотношение сторон")
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
