from .pages.ya_main_page import YaMainPage


LINK = "https://ya.ru"
TENZOR_SITE_LINK = "https://tensor.ru/"


def test_check_search_field_exist(browser):
    """
    Тест - Проверка существования поля поиска
    :param browser:
    :return:
    """
    page = YaMainPage(browser, LINK)
    page.open()
    page.doit_input_text_to_search_field()


def test_check_suggestion_table_exist(browser):
    """
    Тест - Проверка появления поля с подсказками при вводе текста в строке поика
    :param browser:
    :return:
    """
    page = YaMainPage(browser, LINK)
    page.open()
    page.doit_input_text_to_search_field()
    page.should_be_suggestion_table()


def test_check_go_to_search_result_page(browser):
    """
    Тест - проверка появления страницы с результатми поиска
    :param browser:
    :return:
    """
    page = YaMainPage(browser, LINK)
    page.open()
    page.doit_input_text_to_search_field()
    page.doit_go_to_search_result_page()


def test_check_first_link_from_search_result_page(browser):
    """
    Тест - проверка первой ссылки из результатов поиска
    :param browser:
    :return: сооветствие между эталонной ссылкой и фактической
    """
    page = YaMainPage(browser, LINK)
    page.open()
    page.doit_input_text_to_search_field()
    page.doit_go_to_search_result_page()
    res = page.get_first_links_from_search_result_page()
    assert res == TENZOR_SITE_LINK, f"expexted {TENZOR_SITE_LINK}, but get {res}"
