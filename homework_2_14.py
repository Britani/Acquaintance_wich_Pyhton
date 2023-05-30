# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("введите число: "))
even_degrees = 2
count = 1
while number >= 2**count:
    even_degrees = 2 ** count
    print(even_degrees)
    count += 1
    # if number>even_degrees**(count+1):
    #     print(even_degrees)

