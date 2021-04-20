

def digitalRoot(iNumber):
  totalSum = int(iNumber)
  iNumber = str(iNumber)
  
  while totalSum > 10:
    totalSum = 0
    for iNo in iNumber:
      totalSum+=int(iNo)
      
    iNumber = str(totalSum)

  return totalSum


iNumber = str(input("Enter the number:"))

print("The digital root of is:{}".format(digitalRoot(iNumber)))


  