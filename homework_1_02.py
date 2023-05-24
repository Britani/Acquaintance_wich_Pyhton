# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

x = int(input('Введите трехзначное число: '))
sum_numbers = ((x - x % 100) / 100) + (((x - x % 10) - (x - x % 100)) / 10) + x % 10
# print(type(sum_numbers))
sum_numbers = int(sum_numbers)
print(f'Сумма всех чисел этого числа равна {sum_numbers}')
