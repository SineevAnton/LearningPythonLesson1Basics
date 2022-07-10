# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

coordsA = input("Enter the point A coordinates, separeted with comma (Example: 1,2): ").split(',')
coordsB = input("Enter the point B coordinates, separeted with comma (Example: 1,2): ").split(',')
print(coordsA)
print(float(coordsB[-1]))
print("Distance between points is {:.2f}".format(((float(coordsA[0]) - float(coordsB[0]))**2 + (float(coordsA[-1]) - float(coordsB[-1]))**2)**0.5))