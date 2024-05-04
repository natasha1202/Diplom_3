import allure
import pytest

from page_object.page_locators.main_page_locators import MainPageLocators
from page_object.pages.constructor_page import ConstructorPage
from page_object.pages.main_page import MainPage


class TestConstructor:

    @allure.title('По клику на ингредиент открывается окно с детальным описанием ингредиента')
    @allure.description('Пользователь находится на главной странице, кликает по произвольному ингредиенту. '
                        'Открывается окно с детальным описанием ингредиента')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_ingredient(self, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        ingredient.click()
        element = constructor_page.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS)
        assert element.text == 'Детали ингредиента'

    @allure.title('Проверка кнопки закрыть окно с детальным описанием ингредиента')
    @allure.description('Пользователь находится на главной странице, кликает по произвольному ингредиенту. '
                        'Открывается окно с детальным описанием ингредиента. '
                        'Пользователь кликает на крестик и окно закрывается.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_close_popup_ingredient_details(self,request, br_driver):
        driver = request.getfixturevalue(br_driver)
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        ingredient.click()
        main_page.click_on_element(MainPageLocators.CLOSE_DETAILS_BUTTON)
        assert constructor_page.is_pop_up_shown() is False

    @allure.title('Проверка счетчика количества ингредиентов, добавленных в заказ')
    @allure.description('Пользователь находится на главной странице, перетаскавает произвольный ингредиент в поле '
                        'заказа. '
                        'Счетчик над ингредиентом увеличивается. '
                        'Для булок счетчик увеличивается на 2, для соусов и начинок на 1.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_check_ingredient_counter(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        constructor_page.drag_ingredient(ingredient)
        expected_value = constructor_page.define_expected_counter_value()
        actual_value = constructor_page.get_actual_counter(ingredient)
        assert expected_value == actual_value






