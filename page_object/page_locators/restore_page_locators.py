from selenium.webdriver.common.by import By


class RestorePageLocators:
    # Заголовок "Восстановление пароля"
    RESTORE_PWD_HEADER = By.XPATH, ".//h2[contains(text(),'Восстановление пароля')]"
    # Поля ввода эл. почты
    EMAIL_INPUT_FIELD = By.XPATH, ".//input[(@type='text')]"
    # Кнопка "Восстановить"
    RESTORE_BUTTON = By.XPATH, ".//button[contains(text(),'Восстановить')]"
    # Текст "Введите код из письма"
    ENTER_OTP_FROM_EMAIL_HINT = By.XPATH, ".//label[contains(text(),'Введите код из письма')]"
    # Кнопка "Сохранить"
    SAVE_BUTTON = By.XPATH, ".//button[contains(text(),'Сохранить')]"

    # Кнопка скрыть/показать пароль
    EYE_ICON = By.XPATH, ".//div[(@class='input__icon input__icon-action')]"
    # Поля ввода пароля
    PWD_INPUT_FIELD = By.XPATH, ".//input[(@type='password')]"

    # Признак явного отображения пароля
    PWD_SHOW_MARK = By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]/preceding-sibling::input"

