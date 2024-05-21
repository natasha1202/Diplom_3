from selenium.webdriver.common.by import By


# Страница "Конструктор" является главной страницей приложения
class MainPageLocators:
    # заголовок Соберите бургер
    FORM_BURGER_TEXT = By.XPATH, ".//h1[contains(text(),'Соберите бургер')]"

    # Список всех ингредиентов на странице
    INGREDIENTS_LIST = By.XPATH, ".//a[contains(@href, '/ingredient/')]"
    # Список булок
    BUNS_LIST = By.XPATH, ".//p[contains(text(),'булка')]/parent::a"
    # Список соусов
    SAUCES_LIST = By.XPATH, ".//p[contains(text(),'Соус')]/parent::a"
    # Список начинок
    FILLINGS_LIST = By.XPATH, ".//h2[contains(text(),'Начинки')]/following-sibling::ul/a"

    # Счетчик количества ингредиента в заказе
    INGREDIENT_COUNTER = By.XPATH, ".//div[contains(@class, 'counter')]/p"

    # Поле для перетаскивания ингредиентов
    DRAG_AREA = By.XPATH, ".//span[@class='constructor-element__row']"
    # Название ингредиента в поле для перетаскивания ингредиентов
    SELECTED_INGREDIENT_NAME = By.XPATH, ".//span[@class='constructor-element__text']"
    # Кнопка "Оформить заказ"
    SUBMIT_ORDER_BUTTON = By.XPATH, ".//button[contains(text(),'Оформить заказ')]"

    # Текст "Ваш заказ начали готовить"
    ORDER_INFO_SUCCESS = By.XPATH, ".//p[starts-with(@class, 'undefined text text_type_main-small')]"
    # Номер созданного заказа
    ORDER_NUMBER = By.XPATH, ".//h2[contains(@class,'Modal_modal__title_shadow')]"
    # Текст "идентификатор заказа"
    ORDER_ID_TEXT = By.XPATH, ".//p[contains(@class,'undefined text text_type_main-medium')]"
    # Кнопка "Крестик" на форме с сообщением об успешном заказе
    ORDER_MODAL_FORM_CLOSE_BUTTON = By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified')]"

    # Заголовок всплывающего окна "Детали ингредиента"
    INGREDIENT_DETAILS = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_modified')]"
    # Кнопка "Крестик" во всплывающем окне "Детали ингредиента"
    CLOSE_DETAILS_BUTTON = By.XPATH, ".//button[@type='button']"

    # Кнопка входа на главной странице
    LOGIN_BUTTON_DASHBOARD = By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]"


