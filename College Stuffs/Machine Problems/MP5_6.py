def charCount(strSentence):
  iCount = 0
  for letter in strSentence:
    if letter.isalnum():
      iCount+=1
      
  return iCount

def strRev(strSentence):
  return strSentence[::-1]

def removePunctuations(strSentence):
  strRet = ""
  for letter in strSentence:
    if letter.isalnum() or letter.isspace():
      strRet+=letter
      
  return strRet

def getIndexOfLastChar(strSentence):
  iIndex = 0
  for i in range(len(strSentence)):
    if strSentence[i].isalnum():
      iIndex = i
      
  return iIndex

def getIndexOfFirstChar(strSentence):
  iIndex = 0
  for i in range(len(strSentence)):
    if strSentence[i].isalnum():
      iIndex = i
      break
      
  return iIndex

def stringPop(iIndex, strSentence):
  return strSentence[0:iIndex:] + strSentence[iIndex + 1::]

strSentence = "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."

print("a ----------")
print("The total number of characters: {}".format(charCount(strSentence)))
print("b ----------")
for _ in range(10):
  print(strSentence)
print("c ----------")
print(strSentence[0])
print("d ----------")
print(strSentence[:3])
print("e ----------")
print(strRev(removePunctuations(strSentence)[-3:]))
print("f ----------")
print(strRev(strSentence))
print("g ----------")
if len(strSentence) >= 16:
  print("Is string")
else:
  print("Not string")
print("h ----------")
strTemp = strSentence
strTemp = stringPop(int(getIndexOfFirstChar(strTemp)), strTemp)
strTemp = stringPop(int(getIndexOfLastChar(strTemp)), strTemp)
print(strTemp)
print("i ----------")
strTemp = strSentence.upper()
print(strTemp)
print("j ----------")
strTemp = strSentence.replace("a", "XXX")
print(strTemp)