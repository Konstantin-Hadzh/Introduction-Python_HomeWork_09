

""" 2) Реализовать функцию, принимающую несколько параметров, описывающих 
    данные пользователя: имя, фамилия, год рождения, город проживания, email, 
    телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой
"""


def user_data(name, lastname, birth_year, city, email, phone):
    return print(f"Имя: {name}, Фамилия: {lastname}, Год рождения: {birth_year},"
                 f" Город проживания: {city}, Email: {email}, Телефон: {phone}")


user_data(
    name = input('Имя: '), lastname = input('Фамилия: '),
    birth_year = input('Год Рождения: '), city = input('Город проживания: '),
    email = input('email: '), phone = input('phone: '),
)