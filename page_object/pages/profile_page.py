import allure

from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.profile_page_locators import ProfilePageLocators
from page_object.pages.base_page import BasePage
from page_object.pages.login_page import LoginPage


class ProfilePage(BasePage):

    @allure.step("Авторизация в системе")
    def login(self, user):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.set_text_to_element(LoginPageLocators.LOGIN_EMAIL, user.get('email'))

    @allure.step("Перейти к истории")
    def go_to_history(self):
        self.find_element_with_wait(ProfilePageLocators.PROFILE_ORDERS_HISTORY)
        self.click_on_element(ProfilePageLocators.PROFILE_ORDERS_HISTORY)
        self.wait()

    @allure.step("Выбрать заказ из истории заказов")
    def choose_order_from_history(self):
        self.wait()
        order = self.find_element_with_wait(ProfilePageLocators.HISTORY_ORDER_NUMBERS_LIST)
        return order.text

