'''

Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

'''


def someone(name, surname, age, city, email, phone):
    print(f"Name:{name}. Surname: {surname}. Age: {age} years old. Lives in {city}. Email: {email}. Phone: {phone}")


someone('Poul', 'Lodyagin', 31, 'Saint-P', '@mail', '555-55-55')
