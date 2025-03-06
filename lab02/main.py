with open("input.txt", "r") as file:
  lines = file.readlines()

biglist = []

for line in lines:
  smlist = list(map(int, line.split()))
  biglist.append(smlist)

def isSafe(smlist):
  inc = True
  dec = True
  for i in range(len(smlist)-1):
    if smlist[i] >= smlist[i+1]:
      inc = False
    if smlist[i] <= smlist[i+1]:
      dec = False
    if abs(smlist[i]-smlist[i+1]) < 1 or abs(smlist[i]-smlist[i+1]) > 3:
      return False
  return inc or dec

num = 0
for smlist in biglist:
  if isSafe(smlist):
    num +=1
print("Amount of safe lists", num)