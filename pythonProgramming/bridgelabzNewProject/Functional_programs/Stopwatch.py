from Utilities import Utility

try:
    start=int(input("Press 1 to start timer:"))
    if start==1:
        Utility.start()
    else:
        print("Please enter 1 to start timer")
        print("Try after sometime..")

    stop=int(input("Press 0 to stop timer:"))
    if stop==0:
        Utility.stop()
    else:
        exit(0)

    Utility.elapsedTime()
except Exception as e:
    print(e)
