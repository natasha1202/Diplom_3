import allure
import pytest

from page_object.pages.constructor_page import ConstructorPage


class TestConstructor:

    @allure.title('По клику на ингредиент открывается окно с детальным описанием ингредиента')
    @allure.description('Пользователь находится на главной странице, кликает по произвольному ингредиенту. '
                        'Открывается окно с детальным описанием ингредиента')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_click_on_ingredient(self, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        ingredient.click()
        header_text = constructor_page.find_ingredient_details_popup_header()
        assert header_text == 'Детали ингредиента'

    @allure.title('Проверка кнопки закрыть окно с детальным описанием ингредиента')
    @allure.description('Пользователь находится на главной странице, кликает по произвольному ингредиенту. '
                        'Открывается окно с детальным описанием ингредиента. '
                        'Пользователь кликает на крестик и окно закрывается.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_close_popup_ingredient_details(self,request, br_driver):
        driver = request.getfixturevalue(br_driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        ingredient.click()
        constructor_page.ingredient_details_close_popup()
        assert constructor_page.is_pop_up_shown() is False

    @allure.title('Проверка счетчика количества ингредиентов, добавленных в заказ')
    @allure.description('Пользователь находится на главной странице, перетаскивает произвольный ингредиент в поле '
                        'заказа. '
                        'Счетчик над ингредиентом увеличивается. '
                        'Для булок счетчик увеличивается на 2, для соусов и начинок на 1.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_check_ingredient_counter(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.open_main_page()

        ingredient = constructor_page.choose_any_ingredient_from_list()
        constructor_page.drag_ingredient(ingredient)
        expected_value = constructor_page.define_expected_counter_value()
        actual_value = constructor_page.get_actual_counter(ingredient)
        assert expected_value == actual_value






