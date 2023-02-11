from typing import List

# Задача 1
# 2 минут
def cities_string(cities: List) -> str:
    """
    Принимает на вход массив городов. Возвращает строку,
    где города разделены запятыми, а в конце стоит точка.
    """
    cities_str = ", ".join(cities)
    cities_str += "."
    print(cities_str)


cities_string(["Москва", "Санкт-Петербург", "Воронеж"])
# Вывод: Москва, Санкт-Петербург, Воронеж.

# Задача 2
# 18 минут
def myround(x: int or float, base=5) -> int:
    """
    Принимает на вход число и возвращает число, округленное с шагом в 5.
    """
    print(base * round(x / base))


myround(41.7, base=5)
# Вывод: 40

# Задача 3
# 13 минут
def count_of_computers(num: int) -> str:
    """
    Принимает на вход число и возвращает сообщение о количестве компьютеров.
    """
    if num % 100 in [11, 12, 13, 14]:
        print(f"{num} компьютеров")
    elif num % 10 == 1:
        print(f"{num} компьютер")
    elif num % 10 in [2, 3, 4]:
        print(f"{num} компьютера")
    else:
        print(f"{num} компьютеров")
    print(num % 100)


count_of_computers(4892)
# Вывод: 4892 компьютера

# Задача 4
# 7 минут
def simple_numder(num: int) -> str:
    """
    Принимает на вход число и возвращает сообщение о том,
    является ли число простым.
    """
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
    if count > 1:
        print(f"{num} - не простое число")
    else:
        print(f"{num} - простое число")


simple_numder(19)
# Вывод: 19 - простое число

# Задача 5
# 8 минут
def lists(list_1: List, list_2: List) -> List:
    """
    Принимает на вход два массива и возвращает массив с общими элементами.
    """
    list_3 = []
    for i in list_1 and list_2:
        if i in list_1 and i in list_2:
            if list_1.count(i) > 1 and list_2.count(i) > 1:
                list_3.append(i)
    print(list(sorted(set(list_3))))


lists([7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1])
# Вывод: [1, 17]

# Задача 6
# 8 минут
def multiplication_table(num: int) -> int:
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print("%3d" % (i * j), end="")
        print()


multiplication_table(5)
# Вывод:
#  1  2  3  4  5
#  2  4  6  8 10
#  3  6  9 12 15
#  4  8 12 16 20
#  5 10 15 20 25
