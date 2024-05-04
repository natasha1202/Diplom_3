from random import choice

import allure

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class FeedPage(BasePage):

    @allure.step("Открыть страницу Лента заказов")
    def open_feed_page(self):
        locator = FeedPageLocators.FEED_HEADER_TEXT
        feed_page = FeedPage(self.driver)
        feed_page.open_page(locator, PageUrl.FEED_PAGE_URL, feed_page)

    @allure.step("Выбрать заказ из списка")
    def choose_order_from_list(self):
        order = self.driver.find_elements(*FeedPageLocators.ORDER_LIST)
        selected_order = choice(order)
        return selected_order

    @staticmethod
    @allure.step("Вычислить локатор элемента")
    def calculate_locator(number, page_locator):
        method, locator = page_locator
        locator = locator.format(number)
        return method, locator

    @allure.step("Найти заказ по номеру")
    def find_order_by_number(self, number, page_locator):
        order_locator = self.calculate_locator(number, page_locator)
        order = self.driver.find_element(*order_locator)
        return order


