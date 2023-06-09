# RGB-Tools

This is a small repo I thought I'd dump the resources I used to help polish my [latest project Compound Chess](https://fergo310.itch.io/compound-chess)! Below is a Table of Contents for the scripts and resources located in this repo.

##Scripts:

###HEXApplyLum.py
Takes Hexadecimal input, luminance factor, and a mode option ([L]ighten or [D]arken), convert hex to RGB, performs conversions, and then converts RGB back to Hex.

###RGBApplyLum.py
1st draft of ```HEXApplyLum.py```. Takes RGB input instead of Hex.

###RGBConversions.yymps
GameMakerLanguage (GML) package that contains a Decimal to Hex converter ```DecToHex()``` for converting RGB values to Hex.
-Useful for taking Hexadecimal strings as input and converting to color with make_color_rgb()

Also contains ```ColApplyLum()``` which takes ANY color input (#xxxxxx, $xxxxxx, c_color, or make_color_rgb()) and apply luminance factor to it.


##Resources:

[Lode's Computer Graphics Tutorial - Light and Color](https://lodev.org/cgtutor/color.html#RGB_Arithmetic_)
Very helpful source on performing RGB Arithmetic and manipulating RGB values for desired effects.

###RGBToHexEquation.txt
Just some quick notes I took on converting RGB values (decimal) to Hex.
