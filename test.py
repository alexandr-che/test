# Задача 1
my_list = [1, 3, 1, 6, 6, 8, 0, 4, 0, 0, 4, 5, 5, 5, 9, 1, 9]

def unique_list(l):
    return list(set(l))

def unique_list2(l):
    res_list = []
    [res_list.append(i) for i in l if i not in res_list]
    return res_list

print(unique_list(my_list), unique_list2(my_list), sep='\n')


# Задача 2
def list_numbers_in_range(min_num, max_num):
    res_list = [i for i in range(min_num, max_num + 1)]
    return res_list

print(list_numbers_in_range(1, 100))


# Задача 3
import math

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)


point1 = Point(1, 3)
point2 = Point(2, 4)

print(f'Координаты point1 x = {point1.get_x()}, y = {point1.get_y()}')
print(f'Координаты point2 x = {point2.get_x()}, y = {point2.get_y()}')

point1.set_x(5)
point1.set_y(2)

print(f'Координаты point1 после использования методов set_x и set_y: x = {point1.get_x()}, y = {point1.get_y()}')
print(f'Расстояние от point1 до poin2 = {point1.distance(point2)}')


# Задача 4

list_strings = ['a', 'bb', 'ccc', 'dddd', 'eeeee']

def sort_list(l, asc_or_des: int):
    if asc_or_des == 1:
        return sorted(l, key=len)
    return sorted(l, key=len, reverse=True)

print(sort_list(list_strings, 1)) # Список строк по возрастанию
print(sort_list(list_strings, 0)) # Список строк по убываню
