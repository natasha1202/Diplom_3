from random import choice

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Выбор произвольного ингрелиента')
    def choose_any_ingredient_from_list(self):
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENTS_LIST)
        selected_ingredient = choice(ingredients)
        return selected_ingredient

    @allure.step('Выбор булки')
    def choose_bun_from_list(self):
        buns = self.driver.find_elements(*MainPageLocators.BUNS_LIST)
        selected_ingredient = choice(buns)
        return selected_ingredient

    @allure.step('Выбор соуса')
    def choose_sauce_from_list(self):
        sauces = self.driver.find_elements(*MainPageLocators.SAUCES_LIST)
        selected_ingredient = choice(sauces)
        return selected_ingredient

    @allure.step('Выбор начинки')
    def choose_fillings_from_list(self):
        fillings = self.driver.find_elements(*MainPageLocators.FILLINGS_LIST)
        selected_ingredient = choice(fillings)
        return selected_ingredient

    @allure.step('Проверка, показывается ли pop-up')
    def is_pop_up_shown(self):
        return self.is_element_shown(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Перетащить элемент')
    def drag_ingredient(self, moving_element):
        destination_element = self.find_element_with_wait(MainPageLocators.DRAG_AREA)
        action = ActionChains(self.driver)
        action.drag_and_drop(moving_element, destination_element).perform()

    @allure.step('Определение ожидаемго зачения счетчика')
    def define_expected_counter_value(self):
        element = self.find_element_with_wait(MainPageLocators.SELECTED_INGREDIENT_NAME)
        if 'булка' in element.text:
            counter = 2
        else:
            counter = 1
        return int(counter)

    @staticmethod
    @allure.step('Получить значение счетчика ингредиента')
    def get_actual_counter(element):
        p_element = element.find_element(By.XPATH, ".//div[contains(@class, 'counter')]/p")
        return int(p_element.text)

    @allure.step('Сформировать бургер для заказа')
    def form_burger(self):
        bun = self.choose_bun_from_list()
        sauce = self.choose_sauce_from_list()
        filling = self.choose_fillings_from_list()

        self.drag_ingredient(bun)
        self.drag_ingredient(sauce)
        self.drag_ingredient(filling)

        self.wait_for_element_clickable(MainPageLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Создать заказ')
    def create_new_order(self):
        self.form_burger()
        self.click_on_element(MainPageLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Создать заказ и закрыть pop-up с описанием созданного заказа')
    def create_new_order_and_close_popup(self):
        self.create_new_order()
        self.click_on_element(MainPageLocators.ORDER_MODAL_FORM_CLOSE_BUTTON)

    @allure.step('Закрыть pop-up с описанием созданного заказа')
    def new_order_close_popup(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_MODAL_FORM_CLOSE_BUTTON)
        element.click()

    @allure.step('Получить номер нового заказа')
    def get_order_umber(self):
        order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        while order_number == '9999':
            order_number = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        return order_number







