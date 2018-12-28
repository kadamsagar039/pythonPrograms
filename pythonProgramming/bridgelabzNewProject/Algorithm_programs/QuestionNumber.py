from Utilities import Utility
import math
try:
    noOfTimes=int(input("How much time you want to ask the question:"))
    low = 0
    high = int(math.pow(2,noOfTimes))
    print("Think a number between(",low,")to(",high,")in range")
    res=Utility.question(low,high)
    print(res)
except Exception as e:
    print(e)