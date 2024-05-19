import allure

from page_object.page_locators.login_page_locators import LoginPageLocators
from page_object.page_locators.restore_page_locators import RestorePageLocators
from page_object.pages.base_page import BasePage
from page_url import PageUrl


class RestorePage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_restore_page(self):
        locator = RestorePageLocators.EMAIL_INPUT_FIELD
        self.open_page(locator, PageUrl.RESTORE_PAGE_URL)

    @allure.step("Перейти на страницу ввода нового пароля для восстановления пароля")
    def go_to_reset_pwd_page(self, user):
        self.set_text_to_element(RestorePageLocators.EMAIL_INPUT_FIELD, user.get('email'))
        self.wait_for_element(RestorePageLocators.RESTORE_BUTTON)
        self.click_on_element(RestorePageLocators.RESTORE_BUTTON)
        self.wait_for_element(RestorePageLocators.SAVE_BUTTON)

    @allure.step("Перейти на страницу восстановления пароля")
    def go_to_restore_pwd_page_from_login_page(self):
        self.wait_for_element(LoginPageLocators.RESTORE_PWD_LINK)
        self.click_on_element(LoginPageLocators.RESTORE_PWD_LINK)
        self.wait_for_element(RestorePageLocators.RESTORE_BUTTON)
        self.click_on_element(RestorePageLocators.RESTORE_BUTTON)

    @allure.step('Найти заголовок Восстановление пароля')
    def find_restore_header(self):
        return self.get_text_from_element(RestorePageLocators.RESTORE_PWD_HEADER)

    @allure.step('Найти поле для ввода ОТР')
    def find_restore_otp(self):
        return self.find_element_with_wait(RestorePageLocators.ENTER_OTP_FROM_EMAIL_HINT)

    @allure.step('Ввести новый пароль в поле')
    def enter_new_password(self, user):
        self.wait_for_element(RestorePageLocators.EYE_ICON)
        self.set_text_to_element(RestorePageLocators.PWD_INPUT_FIELD, user.get('password'))

    @allure.step('Кликнуть на иконку глаза')
    def click_on_eye_icon(self):
        self.click_on_element(RestorePageLocators.EYE_ICON)

    @allure.step('Получить признак отображения пароля')
    def get_shown_mark(self):
        return self.find_element_without_wait(RestorePageLocators.PWD_SHOW_MARK)










