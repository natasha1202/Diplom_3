import allure

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.page_locators.headers_page_locators import HeadersPageLocators
from page_object.pages.base_page import BasePage


class HeadersPage(BasePage):

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        self.find_element_with_wait(HeadersPageLocators.PROFILE_LINK)
        self.click_on_profile()

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.click_on_feed()
        self.find_feed_text_header_element()

    @allure.step("Перейти в на станицу конструктора")
    def go_to_constructor(self):
        self.click_on_constructor()

    @allure.step('Кликнуть на заголовок "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(HeadersPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на надпись "Лента заказов"')
    def click_on_feed(self):
        self.click_on_element(HeadersPageLocators.FEED_LINK)

    @allure.step('Кликнуть на заголовок "Профиль"')
    def click_on_profile(self):
        self.click_on_element(HeadersPageLocators.PROFILE_LINK)

    @allure.step('Найти заголовок ленты заказов')
    def find_feed_text_header_element(self):
        self.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)

