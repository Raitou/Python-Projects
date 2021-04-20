
iSum = 0

while True:
  iNumber = eval(input("Enter a number (negative to stop):"))
  if iNumber < 0:
    break
  else:
    iSum += iNumber
  
print("Sum is {}".format(iSum))