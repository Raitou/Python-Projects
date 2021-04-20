

def xyz_diff(string_1, string_2):
  iRet = -1
  for i in range(len(string_1)):
    if string_1[i] == string_2[i]:
        continue
      
    iRet = i+1
    break
  
  return iRet

str1 = str(input("Enter first string:"))
str2 = str(input("Enter second string:"))

print(xyz_diff(str1, str2))