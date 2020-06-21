'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
from sys import argv

script_name,  surname, hours, rate, prize = argv

print("Имя скрипта: ", script_name)
print("Фамилия: ", surname)
print("Часы: ", hours)
print("Ставка: ", rate)
print("Премия: ", prize)


def earn():
    print(f"{(surname)} заработал{((int(hours))*(int(rate)) + int(prize)):2}")


earn()
