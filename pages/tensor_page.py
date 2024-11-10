from selenium.webdriver.common.by import By

from .base_page import BasePage


class TensorLocator:
    """
    Определяет локаторы для главной страницы 'Тензор'
    """
    PEOPLE_POWER_SECTION = (By.XPATH, "//*[@class='tensor_ru-Index__block4-bg']/div/div/div/div/p[1]")
    DETAILS_LINK = (By.CSS_SELECTOR, "a[href='/about'].tensor_ru-link")


class TensorPage(BasePage):
    """
    Класс определяющие поведение на главной странице (https://tensor.ru)
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://tensor.ru"

    def verify_strength_in_people(self):
        # Проверка наличия блока "Сила в людях" и переход в "Подробнее"
        strength_block = self.find_element(TensorLocator.PEOPLE_POWER_SECTION)
        assert "Сила в людях" in strength_block.text

    def go_to_about(self):
        """Перейдет в раздел 'О компании' (https://tensor.ru/about)"""
        return self.click(TensorLocator.DETAILS_LINK)
