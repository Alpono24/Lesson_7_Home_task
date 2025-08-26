print("Lesson 7. Home task №2.")
"""
2. Дан список чисел. С помощью filter() получить список тех
элементов из исходного списка, значение которых больше 0.
"""

print(" ")
print("Решение №1 - filter()")
lst_int = [-3, -1, 0, 1, 2, 3]

print(f"Исходный список: {lst_int}")
lst_more_than_zero = list(filter(lambda x: x > 0, lst_int))
print(f"Полученный список (те элементы из исходного списка, значение которых больше 0): {lst_more_than_zero}")

print(" ")
print("Решение №2 - Comprehensions")
lst_int_2 = [-10, -3, -1, 0, 1, 2, -3, 8]
print(f"Исходный список: {lst_int_2}")
lst_more_than_zero_2 = [lst_int_2[i] for i in range(len(lst_int_2)) if lst_int_2[i] > 0 ]
print(f"Полученный список (те элементы из исходного списка, значение которых больше 0): {lst_more_than_zero_2}")
