
strSentence = list("Far far away, behind the word mountains, far from the Countries Vokalia and Consonantia, There live the blind texts.")

strTemp = ""
for i in range(len(strSentence)):
  if (i+1)%2 == 0:
    strSentence[i] = strSentence[i].upper()
    
  strTemp += strSentence[i]
  print(strTemp)
