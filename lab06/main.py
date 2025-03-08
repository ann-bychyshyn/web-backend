with open("input.txt", "r") as file:
  lines = file.readlines()

X = 1
Y = 2
Z = 3
summary = 0
for line in lines:
    com, you = line.split()

    if (com == 'A' and you == 'X') or (com == 'B' and you == 'Y') or (com == 'C' and you == 'Z'):
        rnd = 3
    elif (com == 'A' and you == 'Y') or (com == 'B' and you == 'Z') or (com == 'C' and you == 'X'):
        rnd = 6
    else:
        rnd = 0
    if you == "X":
        shp = X
    elif you == "Y":
        shp = Y
    else:
        shp = Z

    summary += rnd + shp

print('Summary of all rounds - ', summary)