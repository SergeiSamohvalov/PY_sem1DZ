# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите значение координаты X')
X = int(input())
print('Введите значение координаты Y')
Y = int(input())
if Y == 0 or X == 0:
    print('Введите данные координат ОТЛИЧНЫЕ от 0')
if X > 0 and Y > 0:
    print('Точка находится в 1-й четверти плоскости')
elif X > 0 and Y < 0:
    print('Точка находится во 2-й четверти плоскости')
elif X < 0 and Y < 0:
    print('Точка находится в 3-й четверти плоскости')
elif X <0 and Y > 0:
    print('Точка находится в 4-й четверти плоскости')
