from Utilities import Utility
try:
    arr=Utility.inputStringList()
    print(Utility.mergeSort(arr))
except Exception as e:
    print(e)