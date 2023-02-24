import time

from .base_page import BasePage
from selenium.webdriver.common.by import By

MENU_BUTTON_XPATH = "/html/body/main/div[3]/div/a"
PICTURE_BUTTON_CSS = "body > div.popup2.services-more-popup.services-more-popup_bottom_yes.popup2_theme_normal" \
                     ".popup2_autoclosable_yes.popup2_view_classic.i-bem.popup2_js_inited.services-more" \
                     "-popup_js_inited.popup2_visible_yes > div > div > div.scrollbar__scrollable > div > " \
                     "div.services-more-popup__section.services-more-popup__section-all > div > a:nth-child(13)"
PICTURE_BUTTON_LINK = "//yandex.ru/images/"


class YaMainPage(BasePage):

    def should_be_menu_button(self):
        """
        Поиск элемента кнопки меню
        :return:
        """
        self.browser.find_element(By.XPATH, MENU_BUTTON_XPATH)

    def doit_press_pictures_button(self):
        """
        Открытик кнопки меню, поиск элемента картинки, нажатие на элемент картинки
        :return: url открывшейся страницы с картинками
        """
        menu_button = self.browser.find_element(By.XPATH, MENU_BUTTON_XPATH)
        menu_button.click()
        picture_button = self.browser.find_element(By.CSS_SELECTOR, PICTURE_BUTTON_CSS)
        picture_button.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(5)
        current_url = self.browser.current_url
        return current_url

