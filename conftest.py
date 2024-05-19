import pytest
from selenium import webdriver

from api_methods.api_helper import ApiHelper
from data import Data


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
    return Data.user


@pytest.fixture(scope='function')
def registered_user():
    api_helper = ApiHelper()
    new_user = api_helper.register_new_user_and_return_login_password()
    yield new_user
    api_helper.delete_user(new_user)


@pytest.fixture(scope='function')
def create_and_delete_user_with_order(registered_user):
    api_helper = ApiHelper()
    api_helper.create_new_order_by_logged_user_and_return_user(registered_user)
    return registered_user
