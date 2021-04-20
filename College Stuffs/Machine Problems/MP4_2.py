#Name: John Kenneth L. Andales
#School: FEU-TECH
#Machine Problem number - 2


class Circle:
  def __init__(self, radius):
    self.__radius = radius
  
  def area(self):
    return (self.__radius * self.__radius) * 3.14
  
  def perimeter(self):
    return (2 * 3.14) * self.__radius
  
class NegativeValue(Exception):
  pass

class ZeroException(Exception):
  pass

while True:
  try:
    iRadius = int(input("Enter radius:"))
    if iRadius < 0:
      raise NegativeValue()
    elif iRadius == 0:
      raise ZeroException()
      
    circle = Circle(iRadius)
    print("The answer is {}".format(circle.area()))  
    print("Here is the Answer: {}".format(circle.perimeter()))  
    break
  except ValueError:
    print("You use input whole number value:")
  except NegativeValue:
    print("You use enter positive number")
  except ZeroException:
    print("You enter 0 which is not allowed")
  
  