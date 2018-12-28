from Utilities import Utility

try:
    stake=int(input("Enter stake amount:"))
    goal=int(input("Enter goal amount:"))
    noOfTimes=int(input("Enter noOfTimes you want to play:"))
    Utility.gambler(stake,goal,noOfTimes)

except Exception as e:
    print("Wrong input Error:",e)
