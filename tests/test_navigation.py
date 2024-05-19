import allure
import pytest

from page_object.pages.constructor_page import ConstructorPage
from page_object.pages.headers_page import HeadersPage


class TestNavigation:

    @allure.title('Переход с главной страницы на страницу конструктор по клику на надпись Конструктор')
    @allure.description('Пользователь переходит на главную страницу, кликает на надпись конструктор и снова '
                        'оказывается на главной странице ')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_constructor(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        constructor_page = ConstructorPage(driver)
        headers_page = HeadersPage(driver)

        constructor_page.open_main_page()
        headers_page.click_on_constructor()
        assert headers_page.find_constructor_burger_text()

    @allure.title('Переход с главной страницы на страницу Лента заказов по клику на надпись Лента заказов')
    @allure.description('Пользователь переходит на главную страницу, кликает на надпись Лента заказов и '
                        'оказывается на странице с лентой заказов')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_order_feed(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        constructor_page = ConstructorPage(driver)
        headers_page = HeadersPage(driver)

        constructor_page.open_main_page()
        headers_page.click_on_feed()
        feed_header = headers_page.get_feed_header_element()
        assert feed_header == "Лента заказов"

