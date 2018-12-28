
from Utilities import Utility

year=int(input("Enter year(should be 4 digit):"))
if(year > 1000 and year < 9999):
    Utility.leapYear(year)
else:
    print("Enter valid year..")