
def Main():
    try:
        iNumber = int(input("Enter a number: "))
    except ValueError:
        print("Invalid Number")
        Main()
    
    print("The square of " + str(iNumber), str(pow(iNumber, 2)), sep=" is ", end=".\n")

if __name__ == "__main__":
    Main()