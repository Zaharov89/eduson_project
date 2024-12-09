# Ссылка на  colab с данными по уроку
url = 'https://colab.research.google.com/drive/14WRdHxHn_3lZgpeCMYGuEyirvZq1yCsB?usp=sharing#scrollTo=YZCZovbQ8gze'
print(url)

a = 'my string'
print(type(a))

b = 'строка номер 1'
c = 'строка номер 2'
print(b + ' ' + c)  # склеивает две строки с пробелом между ними
print((b + ' ') * 5)  # написать строку b 5 раз подряд

print(len(b))  # найти длину строки

# Примеры вставки кавычек внутрь строки
# Пример 1
d = 'Он сказал ему "Привет!"'  # использоваие разных типов кавычек
print(d)

e = "Он сказал ему \"Привет!\""  # использоваие экранирования
print(e)


# Примеры переноса строки если нужны кавычки
a = """А он сказал: "Привет!"
А она ответила: "Прощай"
"""

b = """
А он сказал: "Привет!"
А она ответила: "Прощай"
"""

c = """
А он сказал: "Привет!" \
А она ответила: "Прощай"
"""

print(a, b, c)

# Как работают спецсимволы?
# \n - перенос строки
# \t - табуляция
print("Это первая строка\nЭто вторая строка\n Это третья строка \t но тут еще табуляция")

# raw string (сырая строка), когда спецсимволы в строке не учитываются как спецсимволы
print(r"Это первая строка\nЭто вторая строка\n Это третья строка \t но тут еще табуляция")


# f строки (чтобы можно было вставлять переменные в текст)
name = "Андрон"
bundle = "Базовый"
days = 365
print(f"""
Привет, {name}!

Вы совершили покупку по тарифу {bundle}! Он будет доступен вам в течение {days} дней.
""")


# форматирование строки (чтобы можно было вставлять переменные в текст)
name = "Андрон"
bundle = "Базовый"
days = 365
print("""
Привет, {0}!

Вы совершили покупку по тарифу {2}! Он будет доступен вам в течение {1} дней.
""".format(name, days, bundle))


# Очистка строк
a = '   abc   '
print(a.strip())  #по дефолту функция strip очищает пустые строки до и после выражения

a = '   abc   x'
print(a.strip(' x'))  #можно указывать, что очищать помимо пробелов


# Разбивка строк по разделителю
keywords = "Python, анализ данных, программирование, я люблю код, ура!"
print(keywords.split(", "))

chapter = """Первое предложение. Второе предложение.
Перенос строки. опять предложение
Опять перенос. Опять предложение."""
print(chapter.split("\n"))


# Объединение строк
arr = ['Меня зовут Андрон', 'Мы с вами изучаем Python', 'Надеюсь, вам интересно']
print('.\n'.join(arr))
# или
print('Меня зовут Андрон' + '.\n' + 'Мы с вами изучаем Python' + '.\n' + 'Надеюсь, вам интересно')


# Изменение регистров букв
s = 'СТРока С ОЧень разныМ РЕГистром букв.'
print(s.capitalize())  # первая заглавная остальные строчные
print(s.upper())  # все заглавные
print(s.lower())  # все строчные


# Проверка наличия символов в начале и в конце строки
s1 = "Обычное предложение."
s2 = "Предложение с  восклицанием!"
print(s1.endswith("!"))
print(s2.endswith("!"))
print(s1.startswith("Обычное"))
print(s2.startswith("Обычное"))


# Поиск подстроки в строке
s = "Длинная строка с некоторым текстом внутри"
print(s.find("некоторым"))  # когда слово есть и найдено (показывает индекс с которого начинается первая буква в тексте
print(s.find('abc'))  # когда слова нет и не найдено


# Замена подстроки в строке
s = "Меня зовут Андрон, Мы с вами изучаем питон, Надеюсь вам нравится"
s = s.replace(',', '.')  # меняет все зпятые на точки
print(s)


# Индексация строк
promocode = '544545foru5066561551'
print(promocode[6:12])


# Срез строки
# [x:y:z] где х - начало среза, y - конец среза (не включительно), z - шаг
text = "Python - замечательный язык программирования!"
print(text[9:22:1])  # вырезать текст в правильном направлении
print(text[22:8:-1])  # вырезать текст в обратном направлении
