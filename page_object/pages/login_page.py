import allure

from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class LoginPage(BasePage):

    @allure.step("Открыть страницу Логина")
    def open_login_page(self):
        locator = LoginPageLocators.LOGIN_FORM_LOGIN_BUTTON
        self.open_page(locator, PageUrl.LOGIN_PAGE_URL)

    @allure.step("Вход в систему под существующим пользователем")
    def login(self, user):
        self.open_login_page()
        self.set_text_to_element(LoginPageLocators.LOGIN_EMAIL, user.get('email'))
        self.set_text_to_element(LoginPageLocators.LOGIN_PASSWORD, user.get('password'))
        self.click_on_element(LoginPageLocators.LOGIN_FORM_LOGIN_BUTTON)
        self.wait_for_element(MainPageLocators.FORM_BURGER_TEXT)



