import os

# with open("recipes.txt") as recipe:
#     for line in recipe:
#         print(line)

# f = open("recipes.txt", "r", encoding="cp1251")
# for line in f:
#     print(line)

# with open('recipes.txt') as f1:
#     print(f1.read())


# with open('recipes.txt', encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines)

f = open("recipes.txt", "rt")
content = f.read()
print(content)gi