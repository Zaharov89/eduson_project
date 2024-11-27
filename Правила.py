from datetime import datetime as dt  # from откуда_импортируем import что_импортируем as как назовем_то_что_импортируем

print(dt.now())

print(
    'Hello world!')  # TODO вот так делаются заметки, что в коде что-либо надо дописать, и оно отражается в нижних инструментах, как стикер

print('Hello world!')  # так оформляется комментарий к строке


# так оформляется комментарий к блоку кода, который пишется ниже
def print_hello_world():
    print('Hello, World')


# Стили имен по PEP8:
# Переменная                                post, new_post
# Функция, метод                            create, do_something
# Класс                                     Model, MyClass
# Константа (неизменяемая переменная)       CONSTANT, MY_CONSTANT
# Модуль                                    module.py, my_module.py


def print_hello_world():
    """Вот так оформляется Docstrings (строки документа).
    В начале всегда идет заглавная буква.
    В конце всегда ставится точка.
    """
    print('Привет, рабочая функция')
