import allure
import pytest

from data import Data
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
        login_page.go_to_restore_pwd_page_from_login_page()
        restore_page.check_restore_page_opened()
        restore_header = restore_page.find_restore_header()
        assert restore_header == 'Восстановление пароля'

    @allure.title('Ввод емейла на странице восстановления пароля и переход на страницу смены пароля')
    @allure.description('Пользователь находится на странице восстановления пароля. '
                        'Пользователь вводит адрес электронной почты в поле Емейл и переходит на страницу ввода '
                        'нового пароля')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_restore_password_enter_email_and_click_restore(self, request, br_driver):
        user = Data.user
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        restore_page.open_restore_page()
        restore_page.go_to_reset_pwd_page(user)
        assert (restore_page.find_restore_otp() and
                driver.current_url == PageUrl.RESET_PAGE_URL)

    @allure.title('Проверка отображения пароля в явном виде')
    @allure.description('Пользователь находится на странице восстановления пароля и переходит на страницу ввода нового '
                        'пароля. '
                        'Пользователь вводит пароль в поле пароль и нажимает на иконку в виде глаза. '
                        'Вместо точек в поле пароль отображается введенный пароль')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_restore_password_click_on_show_pwd(self, request, br_driver):
        user = Data.user
        driver = request.getfixturevalue(br_driver)
        restore_page = RestorePage(driver)
        restore_page.open_restore_page()
        restore_page.go_to_reset_pwd_page(user)

        restore_page.enter_new_password(user)
        restore_page.click_on_eye_icon()
        element = restore_page.get_shown_mark()

        assert element.get_dom_attribute("type") == 'text'

