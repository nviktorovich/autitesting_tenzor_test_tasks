import selenium.common

from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import exceptions

SEARCH_FIELD_XPATH = "/html/body/main/div[2]/form/div[2]/div/input"
SEARCH_BUTTON_XPATH = "/html/body/main/div[2]/form/div[2]/button"
SUGGESTION_TABLE_XPATH = "/html/body/main/div[2]/form/div[3]"
RESULT_LINKS_CSS_SELECTOR = ".Link.Link_theme_outer.Path-Item.link.organic__greenurl"
REQUEST = "Тензор"


class YaMainPage(BasePage):

    def doit_input_text_to_search_field(self):
        """
        Ввод в поле поиска запроса
        :return:
        """
        try:
            search_field = self.browser.find_element(By.XPATH, SEARCH_FIELD_XPATH)
            search_field.send_keys(REQUEST)
            return True, SEARCH_FIELD_XPATH
        except selenium.common.exceptions.NoSuchElementException:
            return False, SEARCH_FIELD_XPATH

    def should_be_suggestion_table(self):
        """
        Поиск всплывающего поля с подсказками
        :return:
        """
        try:
            self.browser.find_element(By.XPATH, SUGGESTION_TABLE_XPATH)
            return True, SUGGESTION_TABLE_XPATH
        except selenium.common.NoSuchElementException:
            return False, SUGGESTION_TABLE_XPATH

    def doit_go_to_search_result_page(self):
        """
        Поиск кнопки найти и нажатие на нее
        :return:
        """
        try:
            search_button = self.browser.find_element(By.XPATH, SEARCH_BUTTON_XPATH)
            search_button.click()
            return True, SEARCH_BUTTON_XPATH
        except selenium.common.exceptions.NoSuchElementException:
            return False, SEARCH_BUTTON_XPATH

    def get_first_links_from_search_result_page(self):
        """
        поиск ссылок в результатах поиска
        :return: первая ссылка из результатов поиска
        """
        results = self.browser.find_elements(By.CSS_SELECTOR, RESULT_LINKS_CSS_SELECTOR)
        return results[0].get_attribute("href")
