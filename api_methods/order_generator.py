import random

import allure
import requests

from api_url import ApiUrl


class OrderGenerator:
    @staticmethod
    @allure.step('Генерируется новый заказ')
    def generate_new_order():
        response = requests.get(ApiUrl.INGREDIENT_INFO_URL)
        ingredients_dict = response.json()

        ingredients_data = ingredients_dict['data']
        ingredients_count = len(ingredients_data)
        ingredients_list = []
        for i in range(0, 3):
            ingredient_index = random.randint(0, ingredients_count-1)
            ingredient = ingredients_data[ingredient_index]
            ingredient_id = ingredient.get('_id')
            ingredients_list.append(ingredient_id)

        order_ingredients = {"ingredients": ingredients_list}
        return order_ingredients

