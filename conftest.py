import pytest
from selenium import webdriver

from api_methods.api_helper import ApiHelper


@pytest.fixture(scope='function')
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = {'email': 'test@ya.ru',
            'password': 'test05',
            'user_name': 'test5'
            }
    return user


@pytest.fixture(scope='function', autouse=True)
def registered_user():
    new_user = ApiHelper.register_new_user_and_return_login_password()
    yield new_user
    ApiHelper.delete_user(new_user)


@pytest.fixture(scope='function', autouse=True)
def create_and_delete_user_with_order():
    new_user = ApiHelper.register_new_user_and_return_login_password()
    ApiHelper.create_new_order_by_logged_user_and_return_user(new_user)
    yield new_user
    ApiHelper.delete_user(new_user)
