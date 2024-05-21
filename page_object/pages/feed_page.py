from random import choice

import allure

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class FeedPage(BasePage):

    @allure.step("Открыть страницу Лента заказов")
    def open_feed_page(self):
        locator = FeedPageLocators.FEED_HEADER_TEXT
        self.open_page(locator, PageUrl.FEED_PAGE_URL)

    @allure.step("Выбрать заказ из списка")
    def choose_order_from_list(self):
        order = self.list_elements(FeedPageLocators.ORDER_LIST)
        selected_order = choice(order)
        return selected_order

    @staticmethod
    @allure.step("Вычислить локатор элемента")
    def calculate_locator(number, page_locator):
        method, locator = page_locator
        locator = locator.format(number)
        return method, locator

    @allure.step("Найти заказ по номеру")
    def find_order_by_number(self, number):
        order_locator = self.calculate_order_locator(number)
        order = self.find_element_without_wait(order_locator)
        return order

    @allure.step("Вычислить локатор заказа на странице")
    def calculate_order_locator(self, order_number):
        order_locator = self.calculate_locator(order_number, FeedPageLocators.ORDER_BY_NUMBER)
        return order_locator

    @allure.step("Найти Popup с информацией по заказу")
    def find_popup_order_details(self):
        return self.find_element_with_wait(FeedPageLocators.MODAL_ORDER_FORM)

    @allure.step('Найти текст заголовка ленты заказов')
    def get_feed_header_element(self):
        element = self.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)
        return element.text

