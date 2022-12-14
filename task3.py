# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
if x>0 and y>0:
    print("Точка находится в 1-ой четверти")
elif x<0 and y>0:
    print("Точка находится во 2-ой четверти")
elif x<0 and y<0:
    print("Точка находится в 3-ой четверти")
elif x>0 and y<0:
    print("Точка находится в 4-ой четверти")
elif x==0 and y==0:
    print("Точка находится в начале координат")
elif x==0 and y!=0:
    print("Точка находится в на оси X")
else:
    print("Точка находится в на оси Y")
