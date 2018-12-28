from Utilities import Utility
from array import *

arr=array('i',[])
length=int(input("Enter length of the array:"))
for i in range(length):
    x=int(input("Enter next element:"))
    arr.append(x)
print(arr)
print()
Utility.findTripplet(arr)
