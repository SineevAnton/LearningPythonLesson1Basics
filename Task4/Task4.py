# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# Write a program, which will accept the number of coordinate quarter
# and return the possible values of x and y coordinates.

possibleValues = {1:"X > 0 and Y > 0", 2:"X < 0 and Y > 0", 3:"X < 0 and Y < 0", 4:"X > 0 and Y < 0"}

while True:
    quarter = int(input("Enter the number of coordinate quarter (from 1 to 4): "))
    if 1 <= quarter <= 4:
        break
    else:
        print("Incorrect input. Please enter the number from 1 to 4.")

print(f"X and Y can be: {possibleValues[quarter]}")