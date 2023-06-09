import math

def clamp(num, minVal, maxVal):
    return max(min(num, maxVal), minVal)

hexVal = str(input("Enter your Hex Code (#xxxxxx):\n")).lstrip("#")
lVal = float(input("Enter your Luminance factor (%):\n"))
mode = input("Do you want to [D]arken or [L]ighten the values?\n")
rgbVals = []

print('RGB =', tuple(int(hexVal[i:i+2], 16) for i in (0, 2, 4)))
rVal = int(hexVal[0:0+2], 16)
gVal = int(hexVal[2:2+2], 16)
bVal = int(hexVal[4:4+2], 16)


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

rCon = clamp(rCon, 0, 255)
gCon = clamp(gCon, 0, 255)
bCon = clamp(bCon, 0, 255)

print()
hexCon = "{:02x}{:02x}{:02x}".format(rCon, gCon, bCon)
print("#{0} -> #{1}".format(hexVal, hexCon))
print("({0}, {1}, {2}) -> ({3}, {4}, {5})".format(int(rVal), int(gVal), int(bVal), int(rCon), int(gCon), int(bCon)))



