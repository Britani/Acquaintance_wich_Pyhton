# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6.

number = int(input('Введите натуральное число больше 1 : '))
if number < 0:
    print('Перечитай условие задачи, затупок')
elif number == 0:
    print('Это первый член последовательности Фибаначи')
elif number == 1:
    print("Это либо 2 либо 3 член последовательности Фибаначи ")
else:
    i = 2
    fib_one = 0
    fib_two = 1
    # answer = 1
    while fib_two < number:
        # fib_one = fib_two
        # fib_two = answer
        # answer = fib_one + fib_two
        fib_one, fib_two = fib_two, fib_one + fib_two,
        i += 1
    if number == fib_two:
        print(i)
    else:
        print(-1)
