
import enum

class Package(enum.Enum):
    INVALID = -1
    A = 0
    B = 1
    C = 2

class PackagePrice(enum.Enum):
    INVALID = -1
    A = 200
    B = 500
    C = 900

class PackagePriceAdd(enum.Enum):
    INVALID = -1
    A = 15
    B = 10
    C = 0

class PackageLimit(enum.Enum):
    INVALID = -255
    A = 10
    B = 20
    C = -1

class Month(enum.Enum):
    INVALID = 0
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
    
g_iPackageType = Package.INVALID
g_iMonth = Month.INVALID
g_iMonthlyHours = 0

def InitPackage(iPackageType):
    global g_iPackageType
    g_iPackageType = iPackageType
    

def InputMonth():
    global g_iMonth
    if not g_iPackageType == Package.C:
        iMonth = Month.INVALID
        try:
            iMonth = Month(int(input("Enter Month(in numerical form M): ")))
            if iMonth == Month.INVALID:
                raise ValueError
        except ValueError:
            print("Invalid selection please enter again")
            InputMonth() 
        g_iMonth = iMonth


def InputHours():
    global g_iMonthlyHours
    if not g_iPackageType == Package.C:
        iMonthlyHours = 0
        try:
            iMonthlyHours = int(input("Enter the number of hours used: "))
            if iMonthlyHours <= 0:
                raise ValueError
        except ValueError:
            print("Invalid selection please enter again")
            InputHours()        
        g_iMonthlyHours = iMonthlyHours

def ProcessPackage():
    iPrice = 0
    dicMonthlyHours = {
        "January" : 744,
        "February" : 672,
        "March" : 744,
        "April" : 720,
        "May" : 744,
        "June" : 720,
        "July" : 744,
        "August" : 744,
        "September" : 720,
        "October" : 744,
        "November" : 720,
        "December" : 744,
        "INVALID" : -1
    }
    iMONTHLY_HOURS_MAX = dicMonthlyHours[g_iMonth.name]
    if g_iPackageType == Package.C:
        iPrice = int(PackagePrice.C.value)
    else:
        if iMONTHLY_HOURS_MAX < g_iMonthlyHours:
            print("Monthly Hours can't be greater than ", iMONTHLY_HOURS_MAX)
            InputHours()
    iMonthlyHours = g_iMonthlyHours
    if g_iPackageType == Package.B:
        iPrice = int(PackagePrice.B.value)
        if PackageLimit.B.value < g_iMonthlyHours:
            iMonthlyHours -= PackageLimit.B.value
            for _ in range(0, iMonthlyHours):
                iPrice += int(PackagePriceAdd.B.value)
    elif g_iPackageType == Package.A:
        iPrice = int(PackagePrice.A.value)
        if PackageLimit.A.value < g_iMonthlyHours:
            iMonthlyHours -= PackageLimit.A.value
            for _ in range(0, iMonthlyHours):
                iPrice += int(PackagePriceAdd.A.value)

    print("Total amount due is Php ", format(float(iPrice), '.2f'))

def Main():
    strPackage = input("Enter Package[A, B, C]: ")
    if type(strPackage) != str:
        print("Invalid selection please enter again")
        Main()
    if strPackage == "A" or strPackage == "a":
        InitPackage(Package.A)
    elif strPackage == "B" or strPackage == "b":
        InitPackage(Package.B)
    elif strPackage == "C" or strPackage == "c":
        InitPackage(Package.C)
    else:
        print("Invalid selection please enter again")
        Main()
    InputMonth()
    InputHours()
    ProcessPackage()


if __name__ == "__main__":
    Main()