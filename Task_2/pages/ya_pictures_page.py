import time
import logging

import selenium.common
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FIRST_PICTURES_CATEGORY_CLASS = "PopularRequestList-Item_pos_0"
SEARCH_FIELD_CLASS = ".input__control.mini-suggest__input"
IMAGE_CLASS = "serp-item__link"
NEXT_BUTTON_CLASS = "CircleButton_type_next"
PREV_ARROW_CLASS = "CircleButton_type_prev"
OPEN_PICTURE_CLASS = "MMImage-Origin"


logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.DEBUG)

# настройка обработчика и форматировщика для logger2
handler1 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter1 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler1.setFormatter(formatter1)
# добавление обработчика к логгеру
logger1.addHandler(handler1)

logger1.info(f"Testing the custom logger for module {__name__}...")


class YaPicturesPage(BasePage):

    def do_it_open_first_category(self):
        """
        Переход в первую категорию картинок
        :return:
        """
        try:
            logger1.debug("start do_it_open_first_category")
            first_category = self.browser.find_element(By.CLASS_NAME, FIRST_PICTURES_CATEGORY_CLASS)
            first_category.click()
            logger1.debug("finish do_it_open_first_category")
            return True
        except selenium.common.exceptions.NoSuchElementException:
            logger1.exception(
                f'exception selenium.common.exceptions.NoSuchElementException, '
                f'not found element with class: {FIRST_PICTURES_CATEGORY_CLASS}')
            return False

    def should_by_category_name_in_search(self):
        """
        Захват названия первой категории, переход в первую категорию картинок, захват появивщегося
        текста в поисковой строке
        :return: название первой категории, текст из поисковой строки
        """
        name_of_first_category, text_from_search_field = "", "another text"
        try:
            logger1.debug("start should_by_category_name_in_search")
            self.browser.implicitly_wait(20)
            first_category = self.browser.find_element(By.CLASS_NAME, FIRST_PICTURES_CATEGORY_CLASS)
            name_of_first_category = first_category.get_attribute("data-grid-text")
            first_category.click()
            search_field = self.browser.find_element(By.CSS_SELECTOR, SEARCH_FIELD_CLASS)
            text_from_search_field = search_field.get_attribute("value")
            logger1.debug("finish should_by_category_name_in_search")
            return name_of_first_category, text_from_search_field
        except selenium.common.exceptions.NoSuchElementException:
            logger1.exception(
                f'exception selenium.common.exceptions.NoSuchElementException, '
                f'not found element with class: {FIRST_PICTURES_CATEGORY_CLASS}'
                f'or not found element with class: {SEARCH_FIELD_CLASS}')
            return name_of_first_category, text_from_search_field

    def do_it_open_first_image(self):
        """
        Переход в первую категорию картинок, нажатие на первую картинку, захват текушего URL
        :return: URL первой открытой картинки
        """
        res = ""
        try:
            logger1.debug("start do_it_open_first_image")
            self.browser.implicitly_wait(10)
            first_category = self.browser.find_element(By.CLASS_NAME, FIRST_PICTURES_CATEGORY_CLASS)
            first_category.click()
            image = self.browser.find_element(By.CLASS_NAME, IMAGE_CLASS)
            image.click()
            time.sleep(5)
            res = self.browser.current_url
            logger1.debug("finish do_it_open_first_image")
            return res
        except selenium.common.exceptions.NoSuchElementException:
            logger1.exception(
                f'exception selenium.common.exceptions.NoSuchElementException, '
                f'not found element with class: {FIRST_PICTURES_CATEGORY_CLASS}'
                f'or not found element with class: {IMAGE_CLASS}')
            return res

    def do_it_push_next_arrow(self):
        """
        Переход в первую категорию, открытие первой картинки, захват названия,
        нажатие на стрелочку вперед, захват названия следующей картинки
        :return: картинка1, картинка2
        """
        logger1.debug("start do_it_push_next_arrow")
        self.browser.implicitly_wait(20)
        first_category = self.browser.find_element(By.CLASS_NAME, FIRST_PICTURES_CATEGORY_CLASS)
        first_category.click()
        image = self.browser.find_element(By.CLASS_NAME, IMAGE_CLASS)
        image.click()
        img1, img2 = "", ""

        try:
            img1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, OPEN_PICTURE_CLASS))
            ).get_attribute("src")
            button = self.browser.find_element(By.CLASS_NAME, NEXT_BUTTON_CLASS)
            button.click()
            img2 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, OPEN_PICTURE_CLASS))
            ).get_attribute("src")
            logger1.debug("finish do_it_push_next_arrow")
            return img1, img2
        except selenium.common.exceptions.NoSuchElementException:
            logger1.exception(f'exception selenium.common.exceptions.NoSuchElementException, not found element with '
                              f'class: {OPEN_PICTURE_CLASS} or not found element with class: {NEXT_BUTTON_CLASS}')
            return img1, img2

    def do_it_push_next_arrow_push_prev_arrow(self):
        """
        Переход в первую категорию, открытие первой картинки, захват названия,
        нажатие на стрелочку вперед, нажатие на стрелочку назад, захват названия картинки
        :return: картинка1, картинка2
        """
        logger1.debug("start do_it_push_next_arrow_push_prev_arrow")
        self.browser.implicitly_wait(20)
        first_category = self.browser.find_element(By.CLASS_NAME, FIRST_PICTURES_CATEGORY_CLASS)
        first_category.click()
        image = self.browser.find_element(By.CLASS_NAME, IMAGE_CLASS)
        image.click()
        img1, img2 = "", "sfdsf"

        try:
            img1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, OPEN_PICTURE_CLASS))
            ).get_attribute("src")
            button_next = self.browser.find_element(By.CLASS_NAME, NEXT_BUTTON_CLASS)
            button_next.click()
            button_prev = self.browser.find_element(By.CLASS_NAME, PREV_ARROW_CLASS)
            button_prev.click()
            img2 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, OPEN_PICTURE_CLASS))
            ).get_attribute("src")
            logger1.debug("finish do_it_push_next_arrow_push_prev_arrow")
            return img1, img2

        except selenium.common.exceptions.NoSuchElementException:
            logger1.exception(f'exception selenium.common.exceptions.NoSuchElementException, not found element with '
                              f'class: {OPEN_PICTURE_CLASS} or not found element with class: {NEXT_BUTTON_CLASS} or '
                              f'not found element with class: {PREV_ARROW_CLASS}')
            return img1, img2

