from selenium.webdriver.common.by import By
from .base_page import BasePage


class ContactsLocator:
    """
    Определяет локаторы для страницы 'Контакты'
    """
    BUTTON_TENSOR = (By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')
    REGION_TEXT_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > span > span")
    PARTNERS = (By.CSS_SELECTOR, "[name='itemsContainer']")
    SHIFT_REGION = (By.CSS_SELECTOR, "[title='Камчатский край']")


class ContactsPage(BasePage):
    """Класс определяющие поведение на странице 'Контакты' (https://sbis.ru/contacts/)"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://sbis.ru/contacts/"

    def go_to_tensor(self):
        """Нажмет на банер 'Тензор' """
        return self.click(ContactsLocator.BUTTON_TENSOR)

    def check_region_user(self, current_region):
        """Сверяет регион на сайте с регионом пользователя (current_region)"""
        self.present_in_element(ContactsLocator.REGION_TEXT_LOCATOR, current_region)
        region = self.find_element(ContactsLocator.REGION_TEXT_LOCATOR).text
        assert region == current_region

    def _get_list_partners(self):
        """Формирует список партнеров"""
        list_partners = []
        for elements in self.find_elements(ContactsLocator.PARTNERS):
            partners = elements.text.split("\n")
            if len(partners) > 1:
                for elem in partners:
                    list_partners.append(elem)

        return list_partners

    def check_partners_is_empty(self):
        """Проверяет что список партнеров не является пустым"""
        lst_part = self._get_list_partners()
        assert len(lst_part) > 0

    def shift_region(self, region):
        """Меняет регион на Камчатский край"""
        self.click(ContactsLocator.REGION_TEXT_LOCATOR)
        self.click(ContactsLocator.SHIFT_REGION)
        self.present_in_element(ContactsLocator.REGION_TEXT_LOCATOR, region)

    def regional_affiliation_partners(self, region):
        """Проверяет принадлежность к региону партнеров"""
        lst_partners = self._get_list_partners()
        for elem in lst_partners:
            if region in elem:
                return True
        raise AssertionError(f"Указанное значение {region} в списке партнеров не найдено.")
