# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

amount_days = int(input("Введите количество рассматриваемых дней: "))
from random import randint

count = 0
maximum_thaw = 0
for i in range(amount_days):
    average_daily_temperature = 1 + randint(-3, 3)
    # average_daily_temperature = randint(-50, 50) - мой вариант
    print(average_daily_temperature)
    if average_daily_temperature >= 0:
        count += 1

    else:
        if maximum_thaw < count:
            maximum_thaw = count

        count = 0
if count > maximum_thaw:
    maximum_thaw = count

print(f"Оттепель  - {maximum_thaw}")