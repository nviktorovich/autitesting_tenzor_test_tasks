from .pages.ya_pictures_page import YaPicturesPage


LINK = "https://yandex.ru/images/"


def test_open_first_category(browser):
    """
    Тест - Открыть первую категорию
    :param browser:
    :return:
    """
    page = YaPicturesPage(browser, LINK)
    page.open()
    res = page.do_it_open_first_category()
    assert res, "не удалось открыть первую категорию картинок"


def test_compare_text_of_category_name_and_text_from_search_field(browser):
    """
    Тест - Проверить, что название категории отображается в поле поиска
    :param browser:
    :return: сравнение текста превью категории и текста из строки поиска после открытия категории
    """
    page = YaPicturesPage(browser, LINK)
    page.open()
    f_class_name, s_text = page.should_by_category_name_in_search()
    assert f_class_name == s_text, f'expected equal names of category and search, ' \
                                   f'got category: {f_class_name}, search: {s_text}'


def test_open_first_image(browser):
    """
    Тест - Открыть 1 картинку, проверить, что картинка открылась
    :param browser:
    :return: выполнение условия, jpg или jpeg теперь в URL
    """
    page = YaPicturesPage(browser, LINK)
    page.open()
    res = page.do_it_open_first_image()
    assert "jpg" in res or "jpeg" in res, f"get {res}, not 'jpg' or 'jpeg' in url"


def test_push_next_arrow_button(browser):
    """
    Тест - Нажать кнопку вперед, проверить, что картинка сменилась
    :param browser:
    :return: выполнения условия, изменения картинки
    """
    page = YaPicturesPage(browser, LINK)
    page.open()
    img1, img2 = page.do_it_push_next_arrow()
    assert img1 != img2, f"expected different img1 and img2, got: 1({img1}), 2({img2}) "


def test_push_next_arrow_button_push_prev_arrow_button(browser):
    """
    Тест - Нажать кнопку вперед и назад, убедиться, что открывается первая картинка
    :param browser:
    :return: сравнение 1 картинки и итоговой картинки
    """
    page = YaPicturesPage(browser, LINK)
    page.open()
    img1, img2 = page.do_it_push_next_arrow_push_prev_arrow()
    assert img1 == img2, f"expected equal img1 and img2, got: 1({img1}), 2({img2})"
