from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Кнопка Выход в профиле
    LOGOUT_BUTTON_PROFILE = By.XPATH, ".//button[contains(text(),'Выход')]"
    # Кнопка Профиль в личном кабинете
    PROFILE_BUTTON_PROFILE = By.XPATH, ".//a[(@href='/account/profile')]"
    # Кнопка "История заказов"
    PROFILE_ORDERS_HISTORY = By.XPATH, ".//a[(@href='/account/order-history')]"
    # Поле Имя в профиле
    NAME_FIELD_PROFILE = By.XPATH, ".//input[(@name='Name')]"

    # Текст профиля "В этом разделе вы можете изменить свои персональные данные"
    PROFILE_INFO_TEXT = By.XPATH, ".//p[contains(@class,'Account_text')]"

    # Список номеров заказов в истории заказов клиента
    HISTORY_ORDER_NUMBERS_LIST = (By.XPATH,
                                  ".//a[contains(@href, '/account/order-history/')]/div/p["
                                  "contains(@class, 'text_type_digits') and last()]")



