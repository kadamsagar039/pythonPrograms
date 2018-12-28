from Utilities import Utility
try:
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    money=int(input("Enter the Amount:"))
    #print(notes)
    Utility.vendingMachine(money,notes)

except Exception as e:
    print(e)