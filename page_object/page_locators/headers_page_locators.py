from selenium.webdriver.common.by import By


class HeadersPageLocators:
    # Кнопка Личный кабинет
    PROFILE_LINK = By.XPATH, ".//a[(@href='/account')]"
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[contains(text(),'Конструктор')]"
    # Кнопка Логотип
    LOGO_LINK = By.XPATH, ".//a[(@href='/')]"
    # Кнопка Лента заказов
    FEED_LINK = By.XPATH, ".//a[(@href='/feed')]"
