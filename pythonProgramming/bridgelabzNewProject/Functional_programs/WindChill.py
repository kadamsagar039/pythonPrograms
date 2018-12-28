from Utilities import Utility
try:
    temp=int(input("Enter temprature in [Fahrenheit]:"))
    windspeed=int(input("Enter wind speed in [mile per hour]:"))
    Utility.windChill(temp,windspeed)
except Exception as e:
    print(e)