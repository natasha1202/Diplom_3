import allure
import pytest

from page_object.pages.constructor_page import ConstructorPage
from page_object.pages.login_page import LoginPage


class TestOrders:

    @allure.title('Сохдание заказа авторизованным пользователем')
    @allure.description('Пользователь авторизуется в системе, на странице конструктора выбирает ингредиенты и '
                        'подтверждает заказ. '
                        'Заказ успешно создан.')
    @pytest.mark.parametrize('br_driver',
                             ['chrome_driver', 'firefox_driver'])
    def test_order_creation_by_logged_user(self, registered_user, request, br_driver):
        driver = request.getfixturevalue(br_driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        login_page.open_login_page()
        login_page.login(registered_user)

        constructor_page.create_new_order()
        info_text = constructor_page.find_order_success_message()

        assert info_text == 'Ваш заказ начали готовить'

