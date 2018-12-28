from Utilities import Utility

try:
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    c=int(input("Enter value of c:"))
    Utility.quadraticFunctionsRoot(a,b,c)
except Exception as e:
    print(e)
