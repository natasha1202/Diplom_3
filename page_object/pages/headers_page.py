import allure

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.page_locators.headers_page_locators import HeadersPageLocators
from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.page_locators.profile_page_locators import ProfilePageLocators
from page_object.pages.base_page import BasePage


class HeadersPage(BasePage):

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        self.find_element_with_wait(HeadersPageLocators.PROFILE_LINK)
        self.click_on_profile()
        self.find_element_with_wait(ProfilePageLocators.PROFILE_BUTTON_PROFILE)

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.click_on_feed()
        self.find_feed_text_header_element()

    @allure.step("Перейти в на станицу конструктора")
    def go_to_constructor(self):
        self.click_on_constructor()
        self.find_element_with_wait(MainPageLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Найти заголовок конструктора бургеров')
    def find_constructor_burger_text(self):
        return self.get_text_from_element(MainPageLocators.FORM_BURGER_TEXT)

    @allure.step('Кликнуть на заголовок "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(HeadersPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Найти заголовок ленты заказов')
    def find_feed_text_header_element(self):
        self.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)

    @allure.step('Найти текст заголовка ленты заказов')
    def get_feed_header_element(self):
        element = self.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)
        return element.text

    @allure.step('Кликнуть на надпись "Лента заказов"')
    def click_on_feed(self):
        self.click_on_element(HeadersPageLocators.FEED_LINK)

    @allure.step('Кликнуть на заголовок "Профиль"')
    def click_on_profile(self):
        self.click_on_element(HeadersPageLocators.PROFILE_LINK)

    @allure.step('Найти заголовок Вход')
    def find_login_header(self):
        return self.find_element_with_wait(LoginPageLocators.LOGIN_HEADER_TEXT)


