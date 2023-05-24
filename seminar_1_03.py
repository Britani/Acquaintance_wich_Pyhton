# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

number_students_first_classroom = int(input('Введите количество учеников в 1 классе: '))
number_students_second_classroom = int(input('Введите количество учеников в 1 классе: '))
number_students_third_classroom = int(input('Введите количество учеников в 1 классе: '))
number_desks = int(((number_students_first_classroom // 2) + (number_students_first_classroom % 2)) + (
            (number_students_second_classroom // 2) + (number_students_second_classroom % 2)) + (
        (number_students_third_classroom // 2) + (number_students_third_classroom % 2)))
print(f"Наименьшее количество парт которое нужно купить равно {number_desks} ")
# Решение в классе
number_desks1 = int((number_students_first_classroom + 1) // 2 + (number_students_second_classroom + 1) // 2 + (
        number_students_third_classroom + 1) // 2)
# если добавить в класс одного человека, то деление на цело будет давать нам нужный результат.
print(f"Наименьшее количество парт которое нужно купить равно {number_desks1} ")
