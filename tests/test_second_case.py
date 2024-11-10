from pages.sbis_page import SbisPage
from pages.contact_page import ContactsPage


def test_go_to_contact(browser):
    """Открывает страницу 'https://sbis.ru' и проверяет корректность перехода в раздел 'Контакты'. """
    sbis = SbisPage(browser)
    sbis.open_website()
    sbis.go_to_contacts()
    sbis.assert_url("https://sbis.ru/contacts")


def test_check_region(browser):
    """ Проверяет корректность отображения региона на странице 'Контакты' """
    contact = ContactsPage(browser)
    contact.open_website()
    contact.check_region_user("Республика Татарстан")


def test_check_list_partners(browser):
    """Открывает страницу 'Контакты' и проверяет что список партнеров не является пустым"""
    contact = ContactsPage(browser)
    contact.open_website()
    contact.check_partners_is_empty()


def test_change_and_check_shift_region(browser):
    """Открывает страницу 'Контакты' меняет регион на '41 Камчатский край' и проверяет корректность смены региона"""
    region = ContactsPage(browser)
    region.open_website()
    region.shift_region("Камчатский край")
    region.check_region_user("Камчатский край")


def test_shift_list_partners(browser):
    """Открывает страницу 'Контакты, меняет регион на '41 Камчатка' и проверяет смену списка партнеров"""
    contact = ContactsPage(browser)
    contact.open_website()
    contact.shift_region("Камчатский край")
    contact.regional_affiliation_partners("Камчатка")


def test_shift_url(browser):
    """Проверяет соответствие адреса сайта после смены региона"""
    contact = ContactsPage(browser)
    contact.open_website()
    contact.shift_region("Камчатский край")
    contact.assert_url("https://sbis.ru/contacts/41-kamchatskij-kraj")
