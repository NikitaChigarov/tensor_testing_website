from selenium.webdriver.common.by import By

from .base_page import BasePage


class AboutLocator:
    """
    Определяет локаторы для страницы 'О компании'
    """
    CHRONOLOGY_PHOTOS = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper img")


class AboutPage(BasePage):
    """
     Класс определяющие поведение для страницы 'О компании' (https://tensor.ru/about)
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://tensor.ru/about"

    def check_photos_dimensions(self):
        """Получает размеры фото по ширине и высоте и сравнивает их"""
        photos = self.driver.find_elements(*AboutLocator.CHRONOLOGY_PHOTOS)
        height_list = [photo.get_attribute("height") for photo in photos]
        width_list = [photo.get_attribute("width") for photo in photos]

        isHeight = True if len(set(height_list)) == 1 else False
        isWidth = True if len(set(width_list)) == 1 else False

        assert isWidth and isHeight
