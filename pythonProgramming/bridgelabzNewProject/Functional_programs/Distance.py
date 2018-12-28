from Utilities import Utility

try:
    x=int(input("Enter value of X:"))
    y=int(input("Enter value of Y:"))
    Utility.distance(x,y)
except Exception as e:
    print(e)