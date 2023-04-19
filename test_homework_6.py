import inspect
from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    if current_time.hour < 7 or current_time.hour > 22:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if current_time.hour < 7 or current_time.hour > 22:
        if dark_theme_enabled_by_user:
            is_dark_theme = True
        else:
            is_dark_theme = False
    elif dark_theme_enabled_by_user:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = [k for k in users for r, t in k.items() if t == 'Olga'][0]
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for k in users:
        for r, t in k.items():
            if type(t) == int and t < 20:
                suitable_users.append(k)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

    print(inspect.getfullargspec(find_registration_button_on_login_page)[0])

def print_a_name(input1, input2):
    input1 = input1.title().replace('_', ' ')
    return f'{input1} [{input2}]'


def open_browser(browser_name):
    actual_result = print_a_name(open_browser.__name__, *inspect.getfullargspec(open_browser)[0])
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_a_name(go_to_companyname_homepage.__name__,
                                 *inspect.getfullargspec(go_to_companyname_homepage)[0])
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_a_name(find_registration_button_on_login_page.__name__,
                                 *inspect.getfullargspec(find_registration_button_on_login_page)[0])

    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"