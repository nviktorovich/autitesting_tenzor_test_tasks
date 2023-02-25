import time

from .pages.ya_main_page import YaMainPage


LINK = "https://ya.ru"
IMAGE_LINK = "https://yandex.ru/images/"


def test_menu_button_on_main_page(browser):
    """
    Тест - проверка открытия страницы яндекса и наличия кнопки меню
    :param browser:
    :return:
    """
    page = YaMainPage(browser, LINK)
    page.open()
    res, selector = page.should_be_menu_button()
    assert res, f"not found element with selector {selector}"


def test_press_picture_button_from_menu(browser):
    """
    Тест - Проверка перехода в из меню в раздел картинки
    :param browser:
    :return: соответствие между прямой ссылкой на яндекс-картинки и фактически открывшейстя страницей
    """
    page = YaMainPage(browser, LINK)
    page.open()
    link = page.doit_press_pictures_button()
    assert link == IMAGE_LINK, f"expected: {IMAGE_LINK}, got: {LINK}"




