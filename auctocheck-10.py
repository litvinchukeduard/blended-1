'''
Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, друге ім'я (або по батькові) та повертає рядок з повним іменем користувача.

Задачі:

    Створіть функцію get_fullname, яка приймає три аргументи: first_name, last_name та middle_name. Зробіть middle_name необов'язковим аргументом зі значенням за замовчуванням "".
    Якщо middle_name передано, функція повинна повертати повне ім'я у форматі 'first_name middle_name last_name'.
    Якщо middle_name не передано, функція повинна повертати повне ім'я у форматі 'first_name last_name'.
    Для формування повного імені використовуйте f-рядок.

Очікуваний результат:

Функція повертає рядок з повним іменем користувача, залежно від того, чи передано друге ім'я.

Підказки:

    Використовуйте умовну конструкцію if для перевірки, чи middle_name не порожній.
    Для створення рядка з повним іменем використовуйте f-рядок для вставки значень змінних.


'''

# first_name = 'John' last_name = 'Doe' -> 'John Doe'

# first_name = 'Dan' last_name = 'Smith' middle_name = 'Alice' -> 'Dan Alice Smith'

def get_fullname_test(first_name: str, last_name: str, middle_name: str) -> str: #| None:
    '''Converts first name, last name, middle name to full name

        - first_name - First name of a person
        - last_name - Last name of a person
        - middle_name - Middle name of a person
    '''
    pass

    
get_fullname_test(1, 1, 1)
print("Works!")

def test_2(first_name, last_name, middle_name=''):
    pass

test_2('John', 'Doe')

def test_3(first_name, *args):
    pass

test_3('John', 1, 2, 3, 4) # 'John', (1, 2, 3, 4)

def test_4(first_name, **kwargs):
    pass

test_4('John', last_name='Doe', middle_name='Alice') # 'John', {'last_name': 'Doe', 'middle_name': 'Alice'}

# def test_2(first_name, middle_name='', last_name):
#     pass

# test_2('John', 'Doe')

# def get_fullname(**kwargs):
#     if 'middle_name' in kwargs:
#         return f'{kwargs['first_name']} {kwargs['middle_name']} {kwargs['last_name']}'
#     else:
#         return f'{kwargs['first_name']} {kwargs['last_name']}'

def get_fullname_kwargs(**kwargs):
    if 'middle_name' in kwargs:
        return f"{kwargs['first_name']} {kwargs['middle_name']} {kwargs['last_name']}"
    return f"{kwargs['first_name']} {kwargs['last_name']}"
        
print(get_fullname_kwargs(first_name='John', last_name='Doe', middle_name='Alice'))

# get_fullname_kwargs('John', 'Doe')

def get_fullname(first_name, last_name, middle_name=''):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    return f"{first_name} {last_name}"
