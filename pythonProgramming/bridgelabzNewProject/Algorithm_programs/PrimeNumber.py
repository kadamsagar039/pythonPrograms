from Utilities import Utility

try:
    start=int(input("Enter start range:"))
    end=int(input("Enter end range:"))
    Utility.isPrime(start,end)
except Exception as e:
    print(e)

