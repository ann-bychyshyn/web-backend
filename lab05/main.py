with open("input.txt", "r") as file:
    lines = file.readlines()

mxred = 12
mxblue = 14
mxgreen = 13
summary = 0

for line in lines:
    strockes = line.split(": ")
    idgame = int(strockes[0].split()[1])
    minisets = strockes[1].split("; ")
    validgame = True

    for miniset in minisets:
        cubes = miniset.split(", ")
        redpoints = 0
        bluepoints = 0
        greenpoints = 0

        for cube in cubes:
            num, color = cube.split()
            num = int(num)
            if color == "red":
                redpoints += num
            elif color == "blue":
                bluepoints += num
            elif color == "green":
                greenpoints += num
        if redpoints > mxred or bluepoints > mxblue or greenpoints > mxgreen:
            validgame = False
            break
    if validgame:
        summary +=idgame
print("Sum of valid games", summary)