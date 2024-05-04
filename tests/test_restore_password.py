import time

import allure
import pytest

from page_object.page_locators.restore_page_locators import RestorePageLocators
from page_object.pages.login_page import LoginPage
from page_object.pages.restore_page import RestorePage
from page_url import PageUrl


class TestRestorePage:

    @allure.title('Переход на страницу восстановления пароля с главной страницы')
    @allure.description('Пользователь находится на странице Входя в систему. '
                        'Пользователь переходит на страницу восстановления пароля по ссылке')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_go_to_restore_page_from_login_page(self, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        login_page = LoginPage(driver)
        login_page.open_login_page()
        restore_page.go_to_restore_pwd_page_from_login_page()
        assert restore_page.get_text_from_element(RestorePageLocators.RESTORE_PWD_HEADER) == 'Восстановление пароля'

    @allure.title('Ввод емейла на странице восстановления пароля и переход на страницу смены пароля')
    @allure.description('Пользователь находится на странице восстановления пароля. '
                        'Пользователь вводит адрес электронной почты в поле Емейл и переходит на страницу ввода '
                        'нового пароля')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_restore_password_enter_email_and_click_restore(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        restore_page.open_restore_page()
        restore_page.go_to_reset_pwd_page(registered_user, RestorePageLocators.SAVE_BUTTON)
        assert (restore_page.find_element_with_wait(RestorePageLocators.ENTER_OTP_FROM_EMAIL_HINT) and
                driver.current_url == PageUrl.RESET_PAGE_URL)

    @allure.title('Проверка отображения пароля в явном виде')
    @allure.description('Пользователь находится на странице восстановления пароля и переходит на страницу ввода нового '
                        'пароля. '
                        'Пользователь вводит пароль в поле пароль и нажимает на иконку в виде глаза. '
                        'Вместо точек в поле пароль отображается введенный пароль')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_restore_password_click_on_show_pwd(self, user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        restore_page.open_restore_page()
        restore_page.go_to_reset_pwd_page(user, RestorePageLocators.SAVE_BUTTON)

        restore_page.wait_for_element(RestorePageLocators.EYE_ICON)
        restore_page.set_text_to_element(RestorePageLocators.PWD_INPUT_FIELD, user.get('password'))
        restore_page.click_on_element(RestorePageLocators.EYE_ICON)
        element = driver.find_element(*RestorePageLocators.PWD_SHOW_MARK)

        assert element.get_dom_attribute("type") == 'text'

    @allure.title('Проверка отображения пароля в явном виде')
    @allure.description('Пользователь находится на странице восстановления пароля и переходит на страницу ввода нового '
                        'пароля. '
                        'Пользователь вводит пароль в поле пароль и дважды нажимает на иконку в виде глаза. '
                        'В поле пароль отображается несколько точек')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver'])
    def test_restore_password_click_on_hide_pwd(self, user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        restore_page.open_restore_page()
        restore_page.go_to_reset_pwd_page(user, RestorePageLocators.SAVE_BUTTON)

        restore_page.wait_for_element(RestorePageLocators.EYE_ICON)
        restore_page.set_text_to_element(RestorePageLocators.PWD_INPUT_FIELD, user.get('password'))
        restore_page.click_on_element(RestorePageLocators.EYE_ICON)
        restore_page.click_on_element(RestorePageLocators.EYE_ICON)
        element = driver.find_element(*RestorePageLocators.PWD_SHOW_MARK)
        assert element.get_dom_attribute("type") == 'password'




