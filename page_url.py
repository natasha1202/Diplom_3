
class PageUrl:
    # Главная страница
    BASE_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
    # Страница профиля клиента "https://stellarburgers.nomoreparties.site/account/profile"
    PROFILE_PAGE_URL = f"{BASE_PAGE_URL}account/profile"
    # Страница логина "https://stellarburgers.nomoreparties.site/login"
    LOGIN_PAGE_URL = f"{BASE_PAGE_URL}login"
    # Страница регистрации "https://stellarburgers.nomoreparties.site/register"
    REGISTRATION_PAGE_URL = f"{BASE_PAGE_URL}register"
    # Страница восстановления пароля "https://stellarburgers.nomoreparties.site/forgot-password"
    RESTORE_PAGE_URL = f"{BASE_PAGE_URL}forgot-password"
    # Страница восстановление пароля с отправкой по емейл  "https://stellarburgers.nomoreparties.site/reset-password"
    RESET_PAGE_URL = f"{BASE_PAGE_URL}reset-password"
    # Страница "Лента заказов" https://stellarburgers.nomoreparties.site/feed
    FEED_PAGE_URL = f"{BASE_PAGE_URL}feed"
