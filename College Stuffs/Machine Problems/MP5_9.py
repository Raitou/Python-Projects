
dictProducts = {}
for i in range(3):
  dictProduct = {}
  strProduct = str(input("enter product name:"))
  iPrice = int(input("enter product price:"))
  dictProduct["strProduct"] = strProduct
  dictProduct["iPrice"] = iPrice
  dictProducts[i] = dictProduct
  print("")


while True:
  strProduct = str(input("enter product name:"))
  for i in range(len(dictProducts)):
    if strProduct == dictProducts[i]["strProduct"]:
      print("price of {} is {}".format(dictProducts[i]["strProduct"], dictProducts[i]["iPrice"]))
      break
  else:
    print("we don't have {}".format(strProduct))
    break
  