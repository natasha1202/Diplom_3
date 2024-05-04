from selenium.webdriver.common.by import By


class FeedPageLocators:

    # Текст заголовка "Лента заказов"
    FEED_HEADER_TEXT = By.CSS_SELECTOR, "h1"

    # Список заказов
    ORDER_LIST = By.XPATH, ".//a[contains(@href, '/feed/')]"

    # Popup с информацией по заказу
    MODAL_ORDER_FORM = By.XPATH, ".//div[starts-with(@class, 'Modal_orderBox')]"

    # Номер заказа
    ORDER_BY_NUMBER = By.XPATH, ".//p[contains(text(), '{}')]"

    # Общее количество заказов
    TOTAL_ORDER_COUNT = By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p"
    # Количество заказов за сегодня
    TODAY_ORDER_COUNT = By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p"



