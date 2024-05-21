import allure

from page_object.page_locators.profile_page_locators import ProfilePageLocators
from page_object.pages.base_page import BasePage


class ProfilePage(BasePage):

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

    @allure.step('Найти текст "В этом разделе вы можете изменить свои персональные данные"')
    def find_profile_text_element(self):
        return self.find_element_with_wait(ProfilePageLocators.PROFILE_INFO_TEXT)

    @allure.step('Кликнуть на заголовок "История заказов"')
    def click_on_history(self):
        self.click_on_element(ProfilePageLocators.PROFILE_ORDERS_HISTORY)

    @allure.step('Найти список заказов')
    def find_users_orders(self):
        elements = self.find_element_without_wait(ProfilePageLocators.PROFILE_ORDERS_HISTORY)
        return elements

    @allure.step('Выйти из системы')
    def logout(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON_PROFILE)


