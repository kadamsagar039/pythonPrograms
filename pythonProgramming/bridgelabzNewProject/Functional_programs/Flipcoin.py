from Utilities import Utility

n=int(input("Enter number of times want to flip a coin:"))
if(n > 0):
    Utility.flipCoins(n)
else:
    print("Enter positive number...")

