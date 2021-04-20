iList = [30, 7, 30, 2, 88, 44, 
         60, 40, 1, 53, 100, 72, 
         86, 64, 40, 85, 3, 19,
         63, 84, 17, 31, 95, 84, 
         99, 60, 85, 74, 65, 38, 
         43, 80, 39, 70, 8, 21, 
         32, 68, 64, 55, 88, 84, 
         49, 68, 70, 98, 21, 51, 
         3, 97]

print("Name: JOHN KENNETH L. ANDALES")
print("School: FEU TECH")
print("Machine Problem - 3")

iEqual = 0
for i in range(len(iList)):
  if iList[i] > 10:
    iList[i] = 666
    iEqual+=1
    
    
print("OUTPUT is {}".format(iList))
print("Total equal values {}".format(iEqual))
print("Total not equal values {}".format(len(iList) - iEqual))