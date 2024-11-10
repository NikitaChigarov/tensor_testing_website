import os

import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

DOWNLOAD_URL = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"


class FileDownloadLocator:
    """Класс описывающий локаторы для страницы (https://sbis.ru/download?tab=plugin&innerTab=ereport25) """
    URL_FILE_LOCATOR = (By.XPATH, "//div[1]/div[2]/div[2]/div/a")


class DownloadFilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://sbis.ru/download?tab=plugin&innerTab=ereport25"

    def get_size_file_on_website(self):
        """Обращается к элементу на сайте для получения размера файла"""
        self.present_in_element(FileDownloadLocator.URL_FILE_LOCATOR, "Скачать")
        size_on_website_lst = self.find_element(FileDownloadLocator.URL_FILE_LOCATOR).text.split(" ")
        size_on_website = float(size_on_website_lst[2])
        return size_on_website

    @classmethod
    def download_file(cls):
        """ Скачивает файл и сохраняет его в директорию download """
        response = requests.get(DOWNLOAD_URL)
        response.raise_for_status()
        with open("download/web_plugin.exe", 'wb') as file:
            file.write(response.content)
        assert os.path.exists("download/web_plugin.exe")

    def check_size_downloaded_file(self):
        """Сравнивает размер файла указанный на сайте с размером скачанного файла"""
        size_on_website = self.get_size_file_on_website()
        size_file = os.path.getsize("download/web_plugin.exe")
        convert_size = round((size_file / 1024) / 1024, 2)
        assert size_on_website == convert_size
