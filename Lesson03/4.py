'''

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

'''
x = 4
y = -2


def my_func():
    return x**y


print(my_func())


def my_another():
    i = 0
    b = 1
    while i <= y:
        return 1 / (x * (x * b))
    b += 1
    i -= 1


print(my_func())
