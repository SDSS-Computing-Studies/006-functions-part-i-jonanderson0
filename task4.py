#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(a):
  return"." not in str(a)

x = isInteger( 9.5 ) == False
print(x)
y = isInteger( -2 ) == True
print(y)
