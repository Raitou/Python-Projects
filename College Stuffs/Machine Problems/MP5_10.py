
strSentence = "By an hadjipogi insisted procured improved am. Paid hadjipogi fine ten now love even hadjipogi. Supplied feelings mr of dissuade recurred no it offering honoured. Am of of in collecting devonshire favourable excellence. Her sixteen end hadjipogi cottage yet reached get hadjipogi invited. Resources hadjipogi sweetness ye do no perfectly. Warmly hadjipogi six one any wisdom. Family giving is hadjipogi beauty chatty highly no. Blessing appetite domestic did mrs hadjipogi rendered entirely. Highly indeed had garden not."

arrDict = ["honoured", "devonshire", "favourable", "improved", "appetite", "hadjipogi"]

def str2asterisk(strword):
  strAst = ""
  for i in strword:
    strAst+="*"
  
  return strAst


for i in arrDict:
  strSentence = strSentence.replace(i , str2asterisk(i))
  
print(strSentence)