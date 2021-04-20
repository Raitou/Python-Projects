
def StarSign(iMonth, iDay):
    """
    convert month/day to int 
    """
    iMonth2Days = iMDay = 0
    if iMonth == 1:
        iMonth2Days = 0
    else:
        if iMonth > 1:
            iMonth2Days += 31
        if iMonth > 2:
            iMonth2Days += 28
        if iMonth > 3:
            iMonth2Days += 31
        if iMonth > 4:
            iMonth2Days += 30
        if iMonth > 5:
            iMonth2Days += 31
        if iMonth > 6:
            iMonth2Days += 30
        if iMonth > 7:
            iMonth2Days += 31
        if iMonth > 8:
            iMonth2Days += 31
        if iMonth > 9:
            iMonth2Days += 30
        if iMonth > 10:
            iMonth2Days += 31
        if iMonth > 11:
            iMonth2Days += 30

    iMDay = iMonth2Days + iDay

    #print(iMDay)

    strStarSign = ""

    #capricorn
    #356 19
    if iMDay >= 356 or iMDay <= 19:
        strStarSign = "Capricorn"
    #aquarius
    #20 49
    elif iMDay >= 20 and iMDay <= 49:
        strStarSign = "Aquarius"
    #pisces
    #50 79
    elif iMDay >= 50 and iMDay <= 79:
        strStarSign = "Pisces"
    #aries
    #80 109
    elif iMDay >= 80 and iMDay <= 109:
        strStarSign = "Aries"
    #taurus
    #110 140
    elif iMDay >= 110 and iMDay <= 140:
        strStarSign = "Taurus"
    #gemini
    #141 171
    elif iMDay >= 141 and iMDay <= 171:
        strStarSign = "Gemini"
    #cancer
    #172 203
    elif iMDay >= 172 and iMDay <= 203:
        strStarSign = "Cancer"
    #leo
    #204 234
    elif iMDay >= 204 and iMDay <= 234:
        strStarSign = "Leo"
    #virgo
    #235 265
    elif iMDay >= 235 and iMDay <= 265:
        strStarSign = "Virgo"
    #libra
    #266 295
    elif iMDay >= 266 and iMDay <= 295:
        strStarSign = "Libra"
    #scorpio
    #296 325
    elif iMDay >= 296 and iMDay <= 325:
        strStarSign = "Scorpio"
    #sagittarius
    #326 #355
    elif iMDay >= 326 and iMDay <= 355:
        strStarSign = "Sagittarius"


    return strStarSign


iMonth = int(input("Please enter your month of birth as a number:"))
iDay = int(input("Please enter your day of birth as a number:"))


strStarSign = StarSign(iMonth, iDay)
print("You are a {}".format(strStarSign)) 

