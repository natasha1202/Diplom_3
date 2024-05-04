import allure

from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class LoginPage(BasePage):

    @allure.step("Открыть страницу Логина")
    def open_login_page(self):
        locator = LoginPageLocators.LOGIN_FORM_LOGIN_BUTTON
        login_page = LoginPage(self.driver)
        login_page.open_page(locator, PageUrl.LOGIN_PAGE_URL, login_page)

    @allure.step("Вход в систему под существующим пользователем")
    def login(self, user):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.set_text_to_element(LoginPageLocators.LOGIN_EMAIL, user.get('email'))
        login_page.set_text_to_element(LoginPageLocators.LOGIN_PASSWORD, user.get('password'))
        login_page.click_on_element(LoginPageLocators.LOGIN_FORM_LOGIN_BUTTON)
        login_page.wait_for_element(MainPageLocators.FORM_BURGER_TEXT)



