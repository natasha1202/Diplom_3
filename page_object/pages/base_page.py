import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Ввести текст")
    def set_text_to_element(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)
        self.wait()

    @allure.step("Подождать пока появится елемент")
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))

    @allure.step("Подождать пока элемент станет возможным кликнуть на элемент")
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            locator
        ))

    @allure.step("Подождать")
    def wait(self):
        WebDriverWait(self.driver, 5)

    @allure.step("Перейти на страницу")
    def go_to_page(self, url):
        page = self.driver.get(url)
        return page

    @allure.step("Открыть страницу кликнув на элемент")
    def open_page(self, locator, page_url, page):
        page.go_to_page(page_url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            locator
        ))
        self.wait()
        return page

    @allure.step("Проверить отображение элемента страницы")
    def is_element_shown(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(
            locator
        ))
        return self.driver.find_element(*locator).is_displayed()

