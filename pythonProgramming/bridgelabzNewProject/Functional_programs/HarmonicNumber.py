
from Utilities import Utility
try:

    n=int(input("Enter a number:"))
    if(n != 0):         #checking no is not zero
        Utility.getHarmonicNumbers(n)
    else:
        print("Enter valid number...")
except Exception as e:
    print("Wrong Input:",e)