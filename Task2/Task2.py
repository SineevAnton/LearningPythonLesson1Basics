# Write a program to check the truthfulness of ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for every predicates values.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ---> \t {(not(x or y or z)) == (not x and not y and not z)}")