# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
number_watermelons = int(input('Введите количество арбузов на рынке : '))
from random import randint

print(f"{number_watermelons} --> ")
min_watermelons = float("+inf")
max_watermelons = float("-inf")
for i in range(number_watermelons):
    watermelon_weight = randint(0, 3000)
    print(f"{watermelon_weight}")
    if min_watermelons > watermelon_weight:
        min_watermelons = watermelon_weight
    if max_watermelons < watermelon_weight:
        max_watermelons = watermelon_weight

print(f"{max_watermelons},{min_watermelons}")
