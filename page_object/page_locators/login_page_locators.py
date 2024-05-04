from selenium.webdriver.common.by import By


class LoginPageLocators:
    # поле ввода пароля
    LOGIN_PASSWORD = By.XPATH, ".//input[(@type='password')]"
    # поле ввода email для входа
    LOGIN_EMAIL = By.XPATH, ".//input[(@name='name')]"

    # кнопка Войти на форме логина
    LOGIN_FORM_LOGIN_BUTTON = By.XPATH, ".//button[contains(text(),'Войти')]"
    # ссылка "Восстановить пароль"
    RESTORE_PWD_LINK = By.XPATH, ".//a[(@href='/forgot-password')]"

    # Заголовок "Вход"
    LOGIN_HEADER_TEXT = By.XPATH, ".//div[starts-with(@class,'Auth_login')]/h2"
