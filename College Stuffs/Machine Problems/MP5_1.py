iList = [63, 52, 10, 42, 32, 17, 
         60, 45, 47, 39, 71, 55, 
         41, 95, 70, 48, 42, 32, 
         13, 35]

print("Name: JOHN KENNETH L. ANDALES")
print("School: FEU TECH")
print("Machine Problem - 1")
print("LIST {}".format(iList))
print("AVERAGE {}".format(sum(iList) / len(iList)))
print("SMALLEST/LARGEST {} {}".format(min(iList), max(iList)))
iTempMin = min(iList)
iTempMax = max(iList)
iList.remove(min(iList))
iList.remove(max(iList))
print("2nd SMALLEST/LARGEST {} {}".format(min(iList), max(iList)))
iList.append(iTempMin)
iList.append(iTempMax)

iEven = 0
iOdd = 0
for i in iList:
  if i % 2 == 0:
    iEven+=1
  else:
    iOdd+=1

print("Total number of Even numbers {}".format(iEven))
print("Total number of Odd numbers {}".format(iOdd))