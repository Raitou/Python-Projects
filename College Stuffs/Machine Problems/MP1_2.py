
width = eval(input("Please enter the width of the field in feet: "))
lenght = eval(input("Please enter the length of the field in feet: "))
sqFeetPerAcre = 0.0

area = width * lenght
sqFeetPerAcre = float(area/43560)

print("The area of the field in acres is {} acres.".format(sqFeetPerAcre))