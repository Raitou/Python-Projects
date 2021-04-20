
iVecPosIntegers = []
iVecCount = 0

while not iVecCount == 5:
    try:
        iPosInteger = int(input("Enter a positive integer: "))
        if iPosInteger <= 0:
            raise ValueError
    except ValueError:
        print("Sorry! You have entered negative integer. Enter positive integers only.")
        continue
    iVecPosIntegers.append(iPosInteger)
    iVecCount+=1

print("The sum of all positive integers entered is ", sum(iVecPosIntegers))