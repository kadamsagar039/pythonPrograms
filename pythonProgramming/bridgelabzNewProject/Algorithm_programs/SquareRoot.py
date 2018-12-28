from Utilities import Utility

try:
    num = int(input("Enter a number:"))
    Utility.sqrt(num)
except Exception as e:
    print(e)
