#Name: John Kenneth L. Andales
#School: FEU-TECH
#Machine Problem number - 3

class RomanNum:
  aiNum = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  astrRom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
  def __init__(self, xNum):
    self.__strRom = ""
    self.__iNum = -1
    if type(xNum) == str:
      self.__strRom = xNum
    elif type(xNum) == int:
      self.__iNum = xNum
  
  @staticmethod
  def romanNumCheck(strRom):
    bRet = True
    for l in strRom:
      if not bRet:
        break
      for ll in RomanNum.astrRom:
        if l == ll:
          bRet = True
          break
        else:
          bRet = False
        
    return bRet
      
        
  
  def Num2Rom(self):
    if self.__iNum < 0:
      return str("Error: You either didn't input a number or you've inputted negative number")
    else:
      iIter = 12 #Maximum Size of aNum and check them every iteration
      iNum = self.__iNum
      strRom = ""
      while iNum > 0:
        x = int(iNum/RomanNum.aiNum[iIter])
        iNum = iNum%RomanNum.aiNum[iIter]
        while x > 0:
          strRom += RomanNum.astrRom[iIter]
          x-=1
        iIter-=1
        
      return strRom
    
  def Rom2Num(self):
    if self.__strRom == "":
      return str("Error: You either didn't input a string or you've inputted none")
    else:
      iIter = 12 #Maximum Size of aNum and check them every iteration
      strRom = self.__strRom
      iNum = 0
      iPrev = 0
      iNext = 0
      for l in range(len(strRom)):
        while iIter >= 0:
          if strRom[l] == RomanNum.astrRom[iIter]:
            iPrev = iNext
            iNext = RomanNum.aiNum[iIter]
            if iNext > iPrev:
               iNum = iNum + (iNext - (iPrev*2))
            else:
              iNum += RomanNum.aiNum[iIter]
            break
          iIter-=1
        iIter = 12
        
      return iNum

class InvalidRoman(Exception):
  pass
    
class MaxValueReached(Exception):
  pass

class ZeroException(Exception):
  pass

class NegativeValue(Exception):
  pass


while True:
  try:
    print("Menu")
    print(" 1.convert an integer to a roman numeral")
    print(" 2.convert a roman numeral to an integer")
    print(" 3.exit")
    iChoice = int(input("Enter your choice:"))
    if iChoice <= 0:
      raise ValueError
    elif iChoice > 3:
      raise ValueError
    elif iChoice == 3:
      break
    while True:
      if iChoice == 1:
        try:
          iInput = int(input("Enter Integer - "))
          if iInput > 5000:
            raise MaxValueReached()
          elif iInput < 0:
            raise NegativeValue()
          elif iInput == 0:
            raise ZeroException()
        except MaxValueReached:
          print("Over Maximum Value which is 5000")
          continue
        except NegativeValue:
          print("Input must be a positive integer")
          continue
        except ZeroException:
          print("Input must not be equals to 0")
          continue
        except ValueError:
          print("Input must be an integer")
          continue
        romanNum = RomanNum(iInput)
        print("Output in Roman numerals is: {}".format(romanNum.Num2Rom()))
        break
      elif iChoice == 2:
        try:
          strInput = str(input("Enter roman numeral - "))
          strInput = strInput.upper()
          if not RomanNum.romanNumCheck(strInput):
            raise InvalidRoman()
          numRoman = RomanNum(strInput)
          print("Output in Integer is - {}".format(numRoman.Rom2Num()))
          break
        except InvalidRoman:
          print("Invalid Roman Numeral")
          continue
  except ValueError:
    print("Invalid Choice")
      
      