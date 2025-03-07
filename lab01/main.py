with open("input.txt", "r") as file:
    lines = file.readlines()

leftli = []
rightli = []

for line in lines:
    num = line.split()
    leftli.append(int(num[0]))
    rightli.append(int(num[1]))

sor_l = sorted(leftli)
sor_r = sorted(rightli)

dis = 0
for i in range(len(sor_l)-1):
    dif = abs(sor_l[i]-sor_r[i])
    dis += dif

print("Distance: ", dis)