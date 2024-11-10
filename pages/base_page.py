from typing import Tuple

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Базовый класс страницы, от которого будут наследоваться все остальные классы тестируемых страниц сайта
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = ""  # ссылка будет определяться в наследуемых классах

    def open_website(self):
        """Откроет браузер на странице self.url"""
        if len(self.url) > 0:
            return self.driver.get(self.url)
        raise ValueError("При наследование от базового класса не была указана ссылка тестируемой страницы.")

    def scroll_page(self, element):
        """Осуществляет скролл страницы до искомого элемента"""
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def present_in_element(self, locator: Tuple[str, str], exp_res, time=10):
        """Ожидает изменения элемента"""
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, exp_res),
                                                      message=f"Невозможно найти элемент по локатору {locator}")

    def find_element(self, locator: Tuple[str, str], time=5):
        """Поиск одного элемента на странице"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Невозможно найти элемент по локатору {locator}")

    def find_elements(self, locator: Tuple[str, str], time=5):
        """Поиск нескольких элемента на странице"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Невозможно найти элементы по локатору {locator}")

    def click(self, locator: Tuple[str, str], time=5):
        """Осуществляет нажатие на элемент"""
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).click()

    def assert_url(self, url):
        """Проверка адреса сайта"""
        assert url in self.driver.current_url
