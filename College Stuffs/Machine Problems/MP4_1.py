#Name: John Kenneth L. Andales
#School: FEU-TECH
#Machine Problem number - 1

class rectangle:
  def __init__(self, length, width):
    self.__length = length
    self.__width = width
    
  def __str__(self):
    return str(self.__length * self.__width)
  

class NegativeValue(Exception):
  pass

class ZeroException(Exception):
  pass

while True:
  try:
    length = int(input("Enter Length value:"))
    width = int(input("Input the width of the rectangle:"))
    if length < 0 or width < 0:
      raise NegativeValue()
    elif length == 0 or width == 0:
      raise ZeroException()
    print("The Area of the Rectangle is:{}".format(rectangle(length, width)))
    break
  except ZeroException:
    print("The number should not be equals to zero:")
  except NegativeValue:
    print("The number is not a positives integer:")
  except ValueError:
    print("Input the correct data format is not a Positive integer:")
  
