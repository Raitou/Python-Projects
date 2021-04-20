
oneLitreOrLess = eval(input("How many bottles have one litre or less: "))
moreThanOneLitre = eval(input("How many bottles have more than one litre: "))


print("The refund for returning these containers is ${:.2f}.".format(float(oneLitreOrLess*.1 + moreThanOneLitre*.25)))

