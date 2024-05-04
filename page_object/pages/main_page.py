import allure

from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        locator = MainPageLocators.FORM_BURGER_TEXT
        main_page = MainPage(self.driver)
        main_page.open_page(locator, PageUrl.BASE_PAGE_URL, main_page)



