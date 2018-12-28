from Utilities import Utility

try:
    n=int(input("Enter a Number:"))
    Utility.primeFactor(n)
except Exception as e:
    print("Something went wrong..",e)



