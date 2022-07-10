# Write a program which accepts coordinates of the point (X and Y),
# where X ≠ 0 and Y ≠ 0 and return the number of coordinates quarter
# to which this point belongs.

while True:
    X = int(input("Enter the X coordinate, different from zero: "))
    Y = int(input("Enter the Y coordinate, different from zero: "))
    if X == 0 or Y == 0:
        print("One or both of coordinates is equal to zero. Please, try again.")
    else:
        break

if X > 0 and Y > 0:
    print("The point belongs to quarter I.")
elif X < 0 and Y > 0:
    print("The point belongs to quarter II.")
elif X < 0 and Y < 0:
    print("The point belongs to quarter III.")
else:
    print("The point belongs to quarter IV.")