"""Реализовать пользовательский
интерфейс с бесконечным циклом"""
from exceptions import *
from func import *
def calculator():
    while True:
        x = input('a = ')
        y = input('b = ')
        if not is_number_invalid(x) or not is_number_invalid(y):
            print('Введите числовое значение!')
            continue

        a = int(x)
        b = int(y)

        if is_divied_by_zero(b):
            print('Деление на ноль!')
            continue
        print(f'Сумма равна, {sum(a, b)}')
        print(f'Разность равна, {sub(a, b)}')
        print(f'Произведение равно, {mult(a, b)}')
        print(f'Частное равно, {divide(a, b)}')
