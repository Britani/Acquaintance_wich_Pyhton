# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_bar_width = int(input('ведите ширину шоколадки: '))
chocolate_bar_length = int(input('ведите длину шоколадки: '))
slice_chocolate = int(input('ведите размер отломанного кусочка: '))

if (slice_chocolate % chocolate_bar_width == 0 or slice_chocolate % chocolate_bar_length == 0) and (
        chocolate_bar_length * chocolate_bar_width) > slice_chocolate:
    print(f'{chocolate_bar_width}  {chocolate_bar_length} {slice_chocolate} --> Да')
else:
    print(f'{chocolate_bar_width}  {chocolate_bar_length} {slice_chocolate} --> Нет')


