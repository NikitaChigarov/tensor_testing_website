from pages.sbis_page import SbisPage
from pages.contact_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage


def test_go_to_contact(browser):
    """Открывает страницу 'https://sbis.ru' и проверяет корректность перехода в раздел 'Контакты'. """
    sbis = SbisPage(browser)
    sbis.open_website()
    sbis.go_to_contacts()
    sbis.assert_url("https://sbis.ru/contacts")


def test_go_to_tensor(browser):
    """
    Перейдет по адресу 'https://sbis.ru/contacts/', нажмет на банер Тензор,
    проверит корректность открытия главной страницы 'https://tensor.ru'
    """
    contacts = ContactsPage(browser)
    contacts.open_website()
    contacts.go_to_tensor()
    browser.switch_to.window(browser.window_handles[-1])
    contacts.assert_url("https://tensor.ru")


def test_check_blok_power_people(browser):
    """Перейдет по адресу 'https://tensor.ru' проверит наличие блока 'Сила в людях'"""
    tensor = TensorPage(browser)
    tensor.open_website()
    tensor.verify_strength_in_people()


def test_tensor_go_to_about(browser):
    """Перейдет по адресу 'https://tensor.ru' проверит корректность перехода в раздел 'О компании' """
    tensor = TensorPage(browser)
    tensor.open_website()
    tensor.go_to_about()
    tensor.assert_url("https://tensor.ru/about")


def test_check_height_and_width(browser):
    """Перейдет по адресу 'https://tensor.ru/about' и проверит размер изображений в блоке 'Работаем' """
    about = AboutPage(browser)
    about.open_website()
    about.check_photos_dimensions()
