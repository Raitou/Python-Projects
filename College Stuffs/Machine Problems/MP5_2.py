iList = [18, 19, 20]

print("Name: JOHN KENNETH L. ANDALES")
print("School: FEU TECH")
print("Machine Problem - 2")
print("Original List {}".format(iList))

iList.pop(1)
iList.insert(1, 17)
print("a {}".format(iList))

iList += [4, 5, 6]
print("b {}".format(iList))

iList.pop(0)
print("c {}".format(iList))

iList.sort()
print("d {}".format(iList))

iList *= 2
print("e {}".format(iList))

iList.pop(3)
iList.insert(3, 25)
print("f {}".format(iList))