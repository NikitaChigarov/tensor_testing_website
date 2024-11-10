from selenium.webdriver.common.by import By

from .base_page import BasePage


class SbisLocator:
    """Клас описывающий локаторы для страницы (https://sbis.ru) """
    BUTTON_CONTACTS = (By.CSS_SELECTOR, "div.sbisru-Header__menu-link")
    MORE_CONTACTS = (By.CSS_SELECTOR, "a[href='/contacts'].sbisru-link")
    DOWNLOAD = (By.CSS_SELECTOR, "[href='/download']")


class SbisPage(BasePage):
    """
    Класс определяющие поведение на главной странице (https://sbis.ru)
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://sbis.ru"

    def go_to_contacts(self):
        """ Нажмет на кнопку 'Контакты' и выберет 'Еще...' """
        self.present_in_element(SbisLocator.BUTTON_CONTACTS, "Контакты")
        self.click(SbisLocator.BUTTON_CONTACTS)
        return self.click(SbisLocator.MORE_CONTACTS)

    def go_to_download(self):
        """Нажмет на кнопку 'Скачать локальные версии' в Footer главной страницы"""
        button = self.find_element(SbisLocator.DOWNLOAD)
        self.scroll_page(button)
        return button.click()
