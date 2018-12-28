from Utilities import Utility

try:
    m=int(input("Enter no of rows:"))
    n=int(input("Enter no of cols:"))
    Utility.accept2DArray(m,n)
except Exception as e:
    print(e)