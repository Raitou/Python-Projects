
iMagnitude = eval(input("Enter an earthquake magnitude:"))

strDesc = ""

if iMagnitude < 2.0:
  strDesc = "Micro"
elif iMagnitude >= 2.0 and iMagnitude < 3.0:
  strDesc = "Very minor"
elif iMagnitude >= 3.0 and iMagnitude < 4.0:
  strDesc = "Minor"
elif iMagnitude >= 4.0 and iMagnitude < 5.0:
  strDesc = "Light"
elif iMagnitude >= 5.0 and iMagnitude < 6.0:
  strDesc = "Moderate"
elif iMagnitude >= 6.0 and iMagnitude < 7.0:
  strDesc = "Strong"
elif iMagnitude >= 7.0 and iMagnitude < 8.0:
  strDesc = "Major"
elif iMagnitude >= 8.0 and iMagnitude < 10.0:
  strDesc = "Great"
elif iMagnitude >= 10.0:
  strDesc = "Meteoric"
  
print("This earthquake is classified as {}".format(strDesc))