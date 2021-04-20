strWord = "abcdefghijklmnopqrstuvwxyz"

print("Name: JOHN KENNETH L. ANDALES")
print("School: FEU TECH")
print("Machine Problem - 4")

iList = []

strLetter = ""
for letter in strWord:
  for j in range(len(iList)+1):
    strLetter += letter
    
  iList.append(strLetter)
  strLetter = ""
  
print("OUTPUT is {}".format(iList))