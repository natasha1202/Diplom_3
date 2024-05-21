#Stellar Burgers

## Список тестов

###Восстановление пароля
Проверь:
переход на страницу восстановления пароля по кнопке «Восстановить пароль» - test_go_to_restore_page_from_login_page
ввод почты и клик по кнопке «Восстановить» - test_restore_password_enter_email_and_click_restore
клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его - test_restore_password_click_on_show_pwd

###Личный кабинет 
Проверь:
переход по клику на «Личный кабинет» - test_click_on_profile_link_user_authorized/test_click_on_profile_link_without_authorization
переход в раздел «История заказов» - test_click_on_orders_history
выход из аккаунта - test_logout

###Проверка основного функционала
Проверь:
переход по клику на «Конструктор» - test_click_on_constructor
переход по клику на «Лента заказов» - test_click_on_order_feed
если кликнуть на ингредиент, появится всплывающее окно с деталями - test_click_on_ingredient 
всплывающее окно закрывается кликом по крестику - test_close_popup_ingredient_details
при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается - test_check_ingredient_counter
залогиненный пользователь может оформить заказ - test_order_creation_by_logged_user

###Раздел «Лента заказов»
Проверь:
если кликнуть на заказ, откроется всплывающее окно с деталями - test_order_popup_details_opening
заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов» - test_user_orders_shown_on_feed_page
при создании нового заказа счётчик Выполнено за всё время увеличивается - test_feed_counter_raised_after_new_order_created
при создании нового заказа счётчик Выполнено за сегодня увеличивается - test_feed_counter_raised_after_new_order_created
после оформления заказа его номер появляется в разделе В работе - test_number_of_new_order_shown_on_feed

## Команды для запуска тестов и отчета
pytest -v tests/ - запуск всех тестов
pytest tests/ --alluredir=allure_results - запуск всех тестов с созданием отчета allure
allure serve allure_results - показать отчет allure в браузере