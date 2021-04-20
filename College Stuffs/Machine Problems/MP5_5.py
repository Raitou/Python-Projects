iList = [2, 5, 11, 2, 10, 
         1, 10, 4, 1, 8, 
         15, 13, 7, 5, 
         6, 5, 7, 6, 13,
        12, 4, 12, 7, 3,
        11, 11, 1, 11, 14,
        12, 9, 4, 1, 7,
        15, 8, 1, 5, 9,
        3, 1, 15, 14, 2,
        11, 1, 2, 3, 7,
        12, 1, 1, 13, 10,
        14, 10, 9, 1, 10,
        9, 14, 3, 1, 13,
        9, 9, 1, 9, 1,
        12, 5, 2, 3, 9,
        15, 9, 12, 10, 10,
        2, 1, 11, 4, 12,
        4, 2, 5, 9, 10,
        6, 15, 6, 13, 13,
        14, 7, 6, 15, 1,
        14 ]


print("Name: JOHN KENNETH L. ANDALES")
print("School: FEU TECH")
print("Machine Problem - 5")
print("ORIGINAL LIST {}".format(iList))

for i in range(len(iList)):
  for j in range(len(iList)):
    if i == j:
      continue
    elif iList[i] == iList[j]:
      iList.pop(j)
      iList.insert(j, "Removed")

iCount = 0
try:
  while True:
    iList.remove("Removed")
    iCount+=1
except ValueError:
  pass

iList.sort(reverse=True)

print("FINAL LIST {}".format(iList))
print("Total Number of remove elements {}".format(iCount))