from Utilities import Utility

try:
    inputNumber=input("Enter a distinct coupon number:")
    list1 = [int(i) for i in str(inputNumber)]
    Utility.coupons(list1)
except Exception as e:
    print(e)