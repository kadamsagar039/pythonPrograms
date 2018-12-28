from Utilities import Utility
try:
    p =int(input("Enter principal amount:"))
    y =int(input("Enter years:"))
    r =int(input("Enter rate of interest:"))
    Utility.monthlyPayment(p, y, r)
except Exception as e:
    print(e)