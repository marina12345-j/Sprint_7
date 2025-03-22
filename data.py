from helpers import generate_login, generate_password, generate_first_name, generate_limit_orders, \
    generate_courier_id

MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_LIST_ORDERS_URL = '/api/v1/orders'
DELETE_COURIER_ENDPOINT = '/api/v1/courier/{courier_id}'

LOGIN = generate_login()
PASSWORD = generate_password()
FIRST_NAME = generate_first_name()
LIMIT_ORDERS = generate_limit_orders()
COURIER_ID = generate_courier_id()

class  NegativeAnswers:
    COURIER_LOGIN_ALREADY_USED = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    OK_TRUE = {'ok': True}


