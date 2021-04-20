iNum = 2

while iNum <= 20:
  print(iNum, end="")
  iNum+=3
  if iNum <= 20:
    print(" ", end="")
  else:
    print("\n", end="")