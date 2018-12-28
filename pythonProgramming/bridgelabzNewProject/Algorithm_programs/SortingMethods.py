from Utilities import Utility
try:

    print("1.binarySearch method for integer")
    print("2.binarySearch method for String")
    print("3.insertionSort method for integer")
    print("4.insertionSort method for String")
    print("5.bubbleSort method for integer")
    print("6.bubbleSort method for String")

    x=int(input("Enter choice:"))
    if x==1:
        val=Utility.inputIntList()
        Utility.start()
        val.sort()
        ele=int(input("Enter element for search:"))
        position=Utility.binarySearch(val, ele)
        if position == -1:
            print("not found")
        else:
            print("found at index", position)
        Utility.stop()
        Utility.elapsedTime()

    elif x==2:
        val = Utility.inputStringList()
        Utility.start()
        val.sort()
        ele = input("Enter element for search:")
        position = Utility.binarySearch(val, ele)
        if position == -1:
            print("not found")
        else:
            print("found at index", position)
        Utility.stop()
        Utility.elapsedTime()
    elif x == 3:
        val=Utility.inputIntList()
        Utility.start()
        print(Utility.insertionSort(val))
        Utility.stop()
        Utility.elapsedTime()

    elif x == 4:
        val = Utility.inputStringList()
        Utility.start()
        print(Utility.insertionSort(val))
        Utility.stop()
        Utility.elapsedTime()

    elif x == 5:
        val=Utility.inputIntList()
        Utility.start()
        print(Utility.bubbleSort(val))
        Utility.stop()
        Utility.elapsedTime()

    elif x == 6:
        val=Utility.inputStringList()
        Utility.start()
        print(Utility.bubbleSort(val))
        Utility.stop()
        Utility.elapsedTime()

    else:
        print("Invalid input...")
except Exception as e:
    print(e)