
class NegativeNumber(Exception):
  def __init__(self):
    pass

class WholeValue(Exception):
  def __init__(self):
    pass

def nextPrimeList(iNum):
  #generate primes up to 100
  arrPrime = []
  for i in range(100):
    if i > 1:
      for j in range(2,i):
        if i % j == 0:
          break
      else:
        arrPrime.append(i)
      
  iRet = 0
  for i in arrPrime:
    if(i == iNum or i > iNum):
      iRet = i
      break
  
  return iRet



try:
  iNum = eval(input("Enter a positive number:"))
  if iNum < 0:
    raise NegativeNumber()
  if type(iNum) == float:
    raise WholeValue()
except NegativeNumber:
  print("The number is not a positive integer")
  iNum = eval(input("Enter a positive integer:"))
except WholeValue:
  print("The number should be whole value.")
  iNum = eval(input("Enter a positive integer:"))


print("The first prime greater than the number entered is:{}".format(nextPrimeList(iNum)))
