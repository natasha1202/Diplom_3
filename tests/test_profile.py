import allure
import pytest

from page_object.page_locators.headers_page_locators import HeadersPageLocators
from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.profile_page_locators import ProfilePageLocators
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage
from page_object.pages.profile_page import ProfilePage


class TestProfile:

    @allure.title('Переход в профиль по нажатию на надпись "Профиль"')
    @allure.description('Зарегестрированный пользователь авторизован и находится на главной странице. '
                        'По клику на надпись Профиль пользователь переходит на страницу профиля')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_profile_link_user_authorized(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(registered_user)
        login_page.click_on_element(HeadersPageLocators.PROFILE_LINK)
        element = profile_page.find_element_with_wait(ProfilePageLocators.PROFILE_INFO_TEXT)
        assert element.text == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Переход в профиль по нажатию на надпись "Профиль" для неавторизованного пользователя')
    @allure.description('Неавторизованный пользователь и находится на главной странице. '
                        'По клику на надпись Профиль пользователь переходит на страницу входа в систему')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_profile_link_without_authorization(self, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_element(HeadersPageLocators.PROFILE_LINK)
        element = profile_page.find_element_with_wait(LoginPageLocators.LOGIN_HEADER_TEXT)
        assert element.text == 'Вход'

    @allure.title('Переход в историю заказов в профиле пользователя')
    @allure.description('Авторизованный пользователь и находится на главной странице. '
                        'Пользователь переходит в профиль, а затем во вкладку История заказов')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_orders_history(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(registered_user)
        login_page.click_on_element(HeadersPageLocators.PROFILE_LINK)
        profile_page.click_on_element(ProfilePageLocators.PROFILE_ORDERS_HISTORY)
        assert ("Account_link_active" in
                driver.find_element(*ProfilePageLocators.PROFILE_ORDERS_HISTORY).get_dom_attribute("class"))

    @allure.title('Авторизованный пользоваетль выходит из системы со страницы профиля')
    @allure.description('Авторизованный пользователь переходит на страницу профиля. '
                        'На странице профиля пользователь кликает на кнопку Выход и оказывается на странице Логина')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_logout(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(registered_user)
        login_page.click_on_element(HeadersPageLocators.PROFILE_LINK)
        profile_page.click_on_element(ProfilePageLocators.LOGOUT_BUTTON_PROFILE)
        element = profile_page.find_element_with_wait(LoginPageLocators.LOGIN_HEADER_TEXT)
        assert element.text == 'Вход'






