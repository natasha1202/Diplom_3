import allure

from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.restore_page_locators import RestorePageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class RestorePage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_restore_page(self):
        locator = RestorePageLocators.EMAIL_INPUT_FIELD
        restore_page = RestorePage(self.driver)
        restore_page.open_page(locator, PageUrl.RESTORE_PAGE_URL, restore_page)

    @allure.step("Перейти на страницу ввода нового пароля для восстановления пароля")
    def go_to_reset_pwd_page(self, user, check_element_locator):
        restore_page = RestorePage(self.driver)
        restore_page.set_text_to_element(RestorePageLocators.EMAIL_INPUT_FIELD, user.get('email'))
        restore_page.wait_for_element(RestorePageLocators.RESTORE_BUTTON)
        restore_page.click_on_element(RestorePageLocators.RESTORE_BUTTON)
        restore_page.wait_for_element(RestorePageLocators.SAVE_BUTTON)
        restore_page.wait_for_element(check_element_locator)

    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_restore_pwd_page_from_login_page(self):
        restore_page = RestorePage(self.driver)
        restore_page.wait_for_element(LoginPageLocators.RESTORE_PWD_LINK)
        restore_page.click_on_element(LoginPageLocators.RESTORE_PWD_LINK)
        restore_page.wait_for_element(RestorePageLocators.RESTORE_BUTTON)
        restore_page.click_on_element(RestorePageLocators.RESTORE_BUTTON)






