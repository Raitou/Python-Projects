
mealAmount = eval(input("Please enter the meal amount excluding tax: $"))
taxRate = .23
tipPercentage = .18

tax = float(mealAmount*taxRate)
tip = float(mealAmount*tipPercentage) 
print("Tax: ${:.2f}.".format(tax))
print("Tip: ${:.2f}.".format(tip))
print("Grand TOTAL: ${:.2f}.".format(mealAmount + tax + tip))