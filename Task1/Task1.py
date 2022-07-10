
# Write a program, which accept the number indicating the day of the week
# and checks whether this day is a weekend.

isWeekend = {1:"No", 2:"No", 3:"No", 4:"No", 5:"No", 6:"Yes", 7:"Yes"}

while True:
    num = int(input("Please enter the day of the week (from 1 to 7). "))
    if 1 <= num <= 7:
        break
    else:
        print("Incorrect input. Please enter the number from 1 to 7")

print(f"Is {num} a weekend day: {isWeekend[num]}")