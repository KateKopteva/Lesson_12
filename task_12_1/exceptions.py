"""Добавить валидацию входных данных"""

def is_number_invalid(number):
    if number.isdigit():
        return True
    else:
        return False
def is_divied_by_zero(number):
    if number == 0:
        return True
    else:
        return False


