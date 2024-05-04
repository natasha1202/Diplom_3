import allure

from page_object.page_locators.feed_page_locators import FeedPageLocators
from page_object.page_locators.headers_page_locators import HeadersPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.page_locators.profile_page_locators import ProfilePageLocators
from page_object.pages.base_page import BasePage


class HeadersPage(BasePage):

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        self.find_element_with_wait(HeadersPageLocators.PROFILE_LINK)
        self.click_on_element(HeadersPageLocators.PROFILE_LINK)
        self.find_element_with_wait(ProfilePageLocators.PROFILE_BUTTON_PROFILE)

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.click_on_element(HeadersPageLocators.FEED_LINK)
        self.find_element_with_wait(FeedPageLocators.FEED_HEADER_TEXT)

    @allure.step("Перейти в на станицу конструктора")
    def go_to_constructor(self):
        self.click_on_element(HeadersPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_with_wait(MainPageLocators.SUBMIT_ORDER_BUTTON)

