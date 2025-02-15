with open("input_1.txt", "r") as file:
    lines = file.readlines()

left_list = []
right_list = []

for line in lines:
    numbers = line.split()
    if len(numbers) == 2: 
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

left_sor = sorted(left_list)
right_sor = sorted(right_list)

dist_sum = 0
for i in range(len(left_sor)):  
    dist_sum += abs(left_sor[i] - right_sor[i])  

print("Сума відстаней:", dist_sum)

scr = 0
for num in left_list:
    count_in_right_list = 0
    for right_num in right_list:
        if right_num == num:
            count_in_right_list += 1
    scr += num * count_in_right_list

print("Показник схожості:", scr)