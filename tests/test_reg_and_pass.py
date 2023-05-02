import pytest
from pages.app import *
from pages.settings import *


@pytest.mark.reg
@pytest.mark.positive
def test_reg_page_open(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/registration"


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
    time.sleep(5)
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин"
    print('Сообщение об ошибке: "Неверный логин')


@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_invalid_email(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_email)   # вводим невалидный адрес электронной почты
    browser.implicitly_wait(10)
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин"


@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_invalid_phone(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_phone)   # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(10)
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин"


@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_invalid_login(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_login)   # вводим невалидный логин
    browser.implicitly_wait(10)
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин"


@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_invalid_ls(browser):
    page = NewPassPage(browser)
    page.tab_ls.click()
    browser.implicitly_wait(2)
    page.enter_username(invalid_ls)   # вводим невалидный номер лицевого счёта
    browser.implicitly_wait(10)
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный формат"
