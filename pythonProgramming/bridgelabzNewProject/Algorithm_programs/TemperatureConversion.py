from Utilities import Utility
try:
    fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
    celsius=float(input("Enter the temperature in celsius:"))
    Utility.temperatureConversion(celsius,fahrenheit)
except Exception as e:
    print(e)