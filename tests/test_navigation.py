import allure
import pytest

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.page_locators.headers_page_locators import HeadersPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.main_page import MainPage


class TestNavigation:

    @allure.title('Переход с главной страницы на страницу конструктор по клику на надпись Конструктор')
    @allure.description('Пользователь переходит на главную страницу, кликает на надпись конструктор и снова '
                        'оказывается на главной странице ')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_constructor(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_element(HeadersPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.find_element_with_wait(MainPageLocators.FORM_BURGER_TEXT)

    @allure.title('Переход с главной страницы на страницу Лента заказов по клику на надпись Лента заказов')
    @allure.description('Пользователь переходит на главную страницу, кликает на надпись Лента заказов и '
                        'оказывается на странице с лентой заказов')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_order_feed(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_element(HeadersPageLocators.FEED_LINK)
        element = main_page.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)
        assert element.text == "Лента заказов"

