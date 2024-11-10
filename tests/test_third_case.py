from pages.sbis_page import SbisPage
from pages.download_page import DownloadFilePage


def test_go_to_download(browser):
    """
    Открывает сайт на главной странице, нажимает на кнопку 'Скачать локальные версии'
    в Footer сайта и проверяет корректность перехода на страницу скачивания
    """
    sbis = SbisPage(browser)
    sbis.open_website()
    sbis.go_to_download()
    sbis.assert_url("https://sbis.ru/download")


def test_download_file():
    """Cкачивает плагин https://sbis.ru/download"""
    DownloadFilePage.download_file()


def test_check_size_file(browser):
    """Проверяет соответствие размера скачанного файл с размером указанным на сайте"""
    file = DownloadFilePage(browser)
    file.open_website()
    file.check_size_downloaded_file()
