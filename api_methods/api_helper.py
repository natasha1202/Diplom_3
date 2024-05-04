import string
import random

import allure
import requests

from api_methods.order_generator import OrderGenerator
from api_url import ApiUrl


class ApiHelper:

    @staticmethod
    @allure.step('Генерация произвольной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Генерируется новый зарегистрированный пользователь')
    def register_new_user_and_return_login_password():
        username = f'k5{ApiHelper.generate_random_string(12)}'
        email = f'{username}@ya.ru'
        password = ApiHelper.generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": username
        }

        response = requests.post(ApiUrl.CREATE_USER_URL, data=payload)
        if response.status_code == 200:
            return payload

    @staticmethod
    @allure.step('Удаление созданного пользователя')
    def delete_user(user):
        token = ApiHelper.login_as_user(user)
        headers = {"Authorization": token}
        requests.delete(ApiUrl.DELETE_USER_URL, headers=headers)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_as_user(login_data):
        response = requests.post(ApiUrl.AUTH_USER_URL, data=login_data)
        access_token = response.json()['accessToken']
        return access_token

    @staticmethod
    @allure.step('Создание нового заказа под зарегестрированным пользовтелем')
    def create_new_order_by_logged_user_and_return_user(user_data):
        order = OrderGenerator.generate_new_order()

        token = ApiHelper.login_as_user(user_data)
        headers = {"Authorization": token}

        response = requests.post(ApiUrl.CREATE_ORDER_URL, headers=headers, data=order)

        return {
            "email": user_data.get('email'),
            "password": user_data.get('password'),
            "name": user_data.get('username')
        }




