

'''5) Реализовать формирование списка, используя функцию range() и возможности 
генератора. В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()'''


from functools import reduce

even_numbers_lst = [el for el in range(1, 10) if el % 2 == 0]
print(even_numbers_lst) # список четных чисел от 100 до 1000

def sum_even_numbers(el2, el):
    return el2 * el
print(reduce(sum_even_numbers, even_numbers_lst)) # список суммы четных чисел     