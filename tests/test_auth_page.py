import pytest
from pages.settings import valid_email, valid_password, invalid_email, invalid_password
from pages.app import *


@pytest.mark.reg
@pytest.mark.positive
def test_auth_page_open(browser):
    page = AuthPage(browser)
    print(f" \nПроверка успешного открытия страницы авторизации")
    assert page.get_relative_link() == "/auth/realms/b2c/protocol/openid-connect/auth"


@pytest.mark.auth
@pytest.mark.positive
def test_auth_email(browser):
    page = AuthPage(browser)
    page.tab_email.click()
    time.sleep(2)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.btn_click_enter()
    assert page.get_relative_link() == "/account_b2c/page"


def test_auth_page_invalid_email(browser):
    page = AuthPage(browser)
    page.enter_username(invalid_email)   # вводим невалидный адрес электронной почты
    page.enter_password(valid_password)   # вводим валидный пароль
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или пароль"
    print(
          f"\nневалидный адрес электронной почты")
    print('Сообщение об ошибке: "Неверный логин или пароль"')


def test_auth_page_invalid_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)   # вводим валидный адрес электронной почты
    page.enter_password(invalid_password)   # вводим невалидный пароль
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или пароль"
    print(f"\n невалидный пароль ")
    print('Сообщение об ошибке: "Неверный логин или пароль"')


def test_auth_by_vk(browser):
    page = AuthPage(browser)
    page.auth_by_vk.click()
    time.sleep(5)
    assert page.get_relative_link() == "/authorize"


def test_auth_by_odhoklassniky(browser):
    page = AuthPage(browser)
    page.auth_by_odnoklassniky.click()
    time.sleep(5)
    assert page.get_relative_link() == "/dk"


def test_auth_by_mail(browser):
    page = AuthPage(browser)
    page.auth_by_mail.click()
    time.sleep(5)
    assert page.get_relative_link() == "/oauth/authorize"


def test_auth_by_google(browser):
    page = AuthPage(browser)
    page.auth_by_google.click()
    time.sleep(5)
    assert page.get_relative_link() == "/o/oauth2/auth/identifier"


def test_auth_by_yandex(browser):
    page = AuthPage(browser)
    page.auth_by_yandex.click()
    time.sleep(5)
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"


@pytest.mark.reg
@pytest.mark.positive
def test_new_pass_page_open(browser):
    page = AuthPage(browser)
    page.forgot_password.click()
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/reset-credentials"


def test_new_pass_invalid_email(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_email)   # вводим невалидный адрес электронной почты
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_email.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-039"
          f"\nНегативный сценарий восстановления пароля по адресу электронной почты: "
          f"невалидный адрес электронной почты")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_email(browser):
    page = NewPassPage(browser)
    page.enter_username(random_email)   # вводим невалидный адрес электронной почты
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_email.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-039"
          f"\nНегативный сценарий восстановления пароля по адресу электронной почты: "
          f"невалидный адрес электронной почты")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-040
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_phone(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_phone)   # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_phone.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-040"
          f"\nНегативный сценарий восстановления пароля по номеру телефона: "
          f"невалидный номер мобильного телефона")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-041
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_login(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_login)   # вводим невалидный логин
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_login.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-041"
          f"\nНегативный сценарий восстановления пароля по логину: "
          f"невалдиный логин")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')


# RTC-042
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_ls(browser):
    page = NewPassPage(browser)
    page.tab_ls.click()
    browser.implicitly_wait(2)
    page.enter_username(invalid_ls)   # вводим невалидный номер лицевого счёта
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной!! ввод символов с картинки
    page.driver.save_screenshot(r"../tests/screenshots/New_password/new_pass_by_wrong_ls.png")
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
    print(f"RTC-042"
          f"\nНегативный сценарий восстановления пароля по номеру лицевого счёта: "
          f"невалидный лицевой счёт")
    print('Сообщение об ошибке: "Неверный логин или текст с картинки"')