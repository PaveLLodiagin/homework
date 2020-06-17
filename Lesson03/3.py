'''

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

'''
a = int(input('Введите первое число : '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

max_numbers = [a, b, c]

max_numbers.pop(min(max_numbers))
print(max_numbers)


def my_func():

    sum = 0
    for i in max_numbers:
        sum += i
    print(sum)


my_func()
