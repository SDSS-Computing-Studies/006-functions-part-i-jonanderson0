#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math

def hypotenuse(a,b,c):
    if c == True:
        return math.sqrt(a**2 + b**2)
    else:
        if a > b:
            return math.sqrt(a**2 - b**2)
        if b > a:
            return math.sqrt(b**2 - a**2)
            
print(hypotenuse(3,4,False))



