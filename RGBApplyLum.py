import math

rVal = float(input("Enter your R value:\n"))
gVal = float(input("Enter your G value:\n"))
bVal = float(input("Enter your B value:\n"))
lVal = float(input("Enter your Luminance factor (%):\n"))
mode = input("Do you want to [D]arken or [L]ighten the values?\n")

if mode.lower() == "d":
    rCon = rVal - int(rVal * (lVal/100))
    gCon = gVal - int(gVal * (lVal/100))
    bCon = bVal - int(bVal * (lVal/100))    
elif mode.lower() == "l":
    rCon = rVal + int(rVal * (lVal/100))
    gCon = gVal + int(gVal * (lVal/100))
    bCon = bVal + int(bVal * (lVal/100))
else:
    print("Invalid Input!")
    quit()

print("({0}, {1}, {2}) -> ({3}, {4}, {5})".format(int(rVal), int(gVal), int(bVal), int(rCon), int(gCon), int(bCon)))



