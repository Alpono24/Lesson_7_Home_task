print("Lesson 7. Home task №1.")
"""
5. Используя map() и reduce() посчитать площадь квартиры,
имея на входе характеристики комнат квартиры. 
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""

rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

from functools import reduce
# for room in rooms:
#     print (room["length"]*room["width"])

#Производим вычисление площадей помещений
square_one = list(map(lambda room: room["length"]*room["width"], rooms))
#Выполняем сложение площадей помещений
square_all = reduce(lambda x, y: x + y, square_one)

print(f"Площадь квартиры равна: {square_all} м2")

