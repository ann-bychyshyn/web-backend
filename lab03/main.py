with open("input.txt", "r") as file:
    lines = file.readlines()

biglist = []
for line in lines:  
    smlist = list(line.strip())
    biglist.append(smlist) 

amnt = 0
for smlist in biglist:
    n = []
    for i in smlist:
        if '0' <= i <= '9':  
            n.append(i)

    if n:
        con = int(n[0]+n[-1])
        amnt += con

print("Total sum: ", amnt)