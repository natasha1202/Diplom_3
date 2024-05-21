import allure
import pytest

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.pages.constructor_page import ConstructorPage
from page_object.pages.feed_page import FeedPage
from page_object.pages.headers_page import HeadersPage
from page_object.pages.login_page import LoginPage
from page_object.pages.profile_page import ProfilePage


class TestFeed:

    @allure.title('Проверка открытия pop-up с детальной информацией о заказе из Ленты заказов')
    @allure.description('Пользователь открывает страницу с лентой заказов и кликает на произвольный заказ. '
                        'В результате открывается pop-up с детальной информацией о заказе')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_order_popup_details_opening(self, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        order = feed_page.choose_order_from_list()
        order.click()

        element = feed_page.find_popup_order_details()
        assert element.is_displayed()

    @allure.title('Проверка, что заказ из истории заказов отображается в ленте')
    @allure.description('Авторизованный пользователь переходит в профиль и просматривает историю своих заказов. '
                        'Произвольным образом выбирает заказ и проверяет, что этот заказ отображается в ленте заказов.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_user_orders_shown_on_feed_page(self, create_and_delete_user_with_order, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        feed_page = FeedPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        headers_page = HeadersPage(driver)

        login_page.open_login_page()
        login_page.login(create_and_delete_user_with_order)

        headers_page.go_to_profile()
        profile_page.go_to_history()
        user_order_number = profile_page.choose_order_from_history()

        headers_page.go_to_feed()
        order_locator = feed_page.calculate_order_locator(user_order_number)

        order = feed_page.find_element_with_wait(order_locator)

        assert order.is_displayed()

    @allure.title('Проверка, что при создании нового заказа увеличивается счетчик заказов на 1')
    @allure.description('Авторизованный пользователь создает новый заказ, переходит в ленту заказов и проверяет, '
                        'что число заказов увелилось на 1. '
                        'Тест параметризованный. Проверяются счетсчики "За Сегодня" и "За все время"')
    @pytest.mark.parametrize('br_driver, counter',
                             [
                                 ('chrome_driver', FeedPageLocators.TOTAL_ORDER_COUNT),
                                 ('firefox_driver', FeedPageLocators.TOTAL_ORDER_COUNT),
                                 ('chrome_driver', FeedPageLocators.TODAY_ORDER_COUNT),
                                 ('firefox_driver', FeedPageLocators.TODAY_ORDER_COUNT)
                             ]
                             )
    def test_feed_counter_raised_after_new_order_created(self, registered_user, request, br_driver, counter):
        driver = request.getfixturevalue(br_driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        headers_page = HeadersPage(driver)

        login_page.open_login_page()
        login_page.login(registered_user)

        headers_page.go_to_feed()
        count_of_orders = feed_page.get_text_from_element(counter)
        headers_page.go_to_constructor()

        constructor_page.create_new_order_and_close_popup()
        headers_page.go_to_feed()

        updated_counter = feed_page.get_text_from_element(counter)
        assert int(updated_counter) == int(count_of_orders) + 1

    @allure.title('Проверка, что новый заказ отображается в ленте заказов')
    @allure.description('Авторизованный пользователь создает новый заказ, переходит в ленту заказов и проверяет, '
                        'что заказ отображается в ленте. '
                        'Тест параметризованный. Проверяются счетсчики "За Сегодня" и "За все время"')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_number_of_new_order_shown_on_feed(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        headers_page = HeadersPage(driver)

        login_page.open_login_page()
        login_page.login(registered_user)

        constructor_page.create_new_order()
        order_number = constructor_page.get_order_number()

        constructor_page.new_order_close_popup()
        headers_page.go_to_feed()

        order_element = feed_page.find_order_by_number(order_number)
        assert order_element.is_displayed() is True
