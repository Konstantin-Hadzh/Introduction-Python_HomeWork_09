

"""
Задание 3.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем 
нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой
"""

class ZeroDivision(Exception):
    def __init__(self, num_str):
        self.num_str = num_str


def split():
    try:
        divisible = int(input('Делимое: '))
        divider = int(input('Делитель: '))
        if divider == 0:
            raise ZeroDivision("Делить на ноль нельзя")
        else:
            quot = divisible / divider
            return quot
    except ValueError:
        return "Вы ввели не число"
    except ZeroDivision as error:
        return error


print(split())