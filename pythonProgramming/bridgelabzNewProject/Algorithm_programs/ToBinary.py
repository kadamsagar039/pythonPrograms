from Utilities import Utility
try:
    num = int(input("Enter a number:"))
    str1 = bin(num).replace("0b","")
    Utility.toBinary(str1)
except Exception as e:
    print(e)
