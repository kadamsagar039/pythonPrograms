import random
import numpy as np
import math
import time

"""Purpose: User Input and Replace String Template “Hello <<UserName>>, How are you?”.
   @author  kadamsagar039
   @version 3.7
   @since   21-12-2018
 """


def username(uname):
    if 3 < len(uname):  # Ensure UserName has min 3 char
        print("Hello", uname, ",How are you")  # replace username
    else:
        print("Enter Valid username...")


"""Purpose: Flip Coin and print percentage of Heads and Tails.
   @author  kadamsagar039
   @version 3.7
   @since   21-12-2018
 """


def flipCoins(n):
    head = 0  # Initialization
    tail = 0
    for x in range(n):
        x = random.random()  # random function give value between 0 to 1.
        if x < 0.5:
            tail += 1  # increment tail by 1
        else:
            head += 1  # increment head by 1

    headPercentage = (head * 100) / n  # Calculating average of heads and tails
    tailPercentage = (tail * 100) / n

    print("Head percentage:", headPercentage)
    print("Tail percentage:", tailPercentage)

    """ Purpose: Leap Year
        @author  kadamsagar039
        @version 3.7
        @since   21-12-2018"""


def leapYear(year):
    # condition for checking leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("This is leap year")
    else:  # print result
        print("This is not leap year")


"""Purpose: Power of 2
   @author  kadamsagar039
   @version 3.7
   @since   21-12-2018
 """


def printTable(n):
    i = 0
    while i <= n:  # loop will iterate till i<=n
        print(i, " -  ", pow(2, i))  # print table
        i += 1  # increment by 1


""" Purpose: Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 
   @author  kadamsagar039
   @version 3.7
   @since   21-12-2018
 """


def getHarmonicNumbers(n):
    sum = 0
    for i in range(1, n, 1):  # loop iterate till input element
        sum = sum + float(1 / i)  # sum calculate value of Nth element

    print("Nth harmonic value:", sum)  # print result


""" Purpose: prime factorization of given number...
   @author  kadamsagar039
   @version 3.7
   @since   22-12-2018
 """


def primeFactor(n):
    for i in range(2, n, 1):
        if n % i == 0:  # if n is divisible by i
            cnt = 0  # Initialize counter to 0
            while n % i == 0:  # while number is divisible by i
                n = n / i  # n will divided by i
                cnt += 1  # Increased counter by 1 each time

            print("prime factors:", i, "^", cnt)  # print factors


"""Purpose: Gambler...
   @author  kadamsagar039
   @version 3.7
   @since   22-12-2018
 """


def gambler(stake, goal, noOfTimes):
    bets = 0
    wins = 0  # Initialization

    for i in range(noOfTimes):
        cash = stake
        while 0 < cash < goal:  # checks cash is greater than 0 and less than goal amount
            bets += 1  # Increment bets
            if random.random() < 0.5:  # if value of random function less than 0.5
                cash += 1  # Increment cash by 1
            else:
                cash -= 1  # decrement cash by 1
    if cash == goal:
        wins += 1  # If cash== goal increment wins by 1

    print(wins, " wins of ", noOfTimes)
    print("Percent of games won =", 100.0 * wins / noOfTimes)  # print wining in percent
    print("Avg # bets           =", 1.0 * bets / noOfTimes)


"""Purpose: Sum of three Integer adds to ZERO...
   @author  kadamsagar039
   @version 3.7
   @since   24-12-2018
 """


def findTripplet(arr):
    n = len(arr)
    cnt = 0
    for i in range(0, n - 2, 1):  # [0, 1, 2, -1, -2]
        for j in range(i + 1, n - 1, 1):  # [i  j  k] increased as per loop conditions
            for k in range(j + 1, n, 1):
                if int(arr[i]) + int(arr[j]) + int(arr[k]) == 0:  # check addition of 3 is zero or not
                    print(arr[i], " ", arr[j], " ", arr[k])  # print set of elements
                    cnt += 1
    if cnt == 0:
        print("Not Exists")


"""Purpose: CouponNumbers...
   @author  kadamsagar039
   @version 3.7
   @since   24-12-2018
 """


def coupons(list1):
    cnt = 0  # initialize counter
    while len(list1) > 0:
        x = random.randint(0, 9)  # generate number between 0-9
        cnt += 1  # increment cnt
        if x in list1:  # check x is present in list or not
            list1.remove(x)  # if matched then remove that
            # print(list1)

    print("Total random number needed to have all distinct numbers:", cnt)


"""Purpose: Accept 2D array...
   @author  kadamsagar039
   @version 3.7
   @since   24-12-2018
 """


def accept2DArray(m, n):
    arr = [[0 for i in range(m)] for j in range(n)]
    # print(arr)

    for i in range(m):
        for j in range(n):
            arr[i][j] = int(input("Enter elements:"))  # integer element
            # arr[i][j] = float(input("Enter elements:")) #float type element

    array = np.array(arr)  # convert into numpy array for matrix
    print(array)  # representation of array


"""Purpose: Quadratic Functions Root
       @author  kadamsagar039
       @version 3.7
       @since   24-12-2018"""


def quadraticFunctionsRoot(a, b, c):
    print("Given quadratic equation:", a, "x^2 +", b, "x +", c)
    d = (b * b) - (4 * a * c)  # calculate value of d
    if d > 0:
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d)) / (2 * a)  # calculate roots
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("First Root", root1)  # print root values
        print("Second Root", root2)

    elif d == 0:
        # if value of d is zero
        print("Roots are real and equal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("First Root", root1)

    else:
        print("Roots are imaginary")


"""Purpose: Calculate distance between two points
       @author  kadamsagar039
       @version 3.7
       @since   24-12-2018"""


def distance(x, y):
    dist = math.sqrt((x * x) + (y * y))  # calculate distance using formula
    print("distance from (", x, ",", y, ") to (0, 0)=", dist)  # print result


"""Purpose: Calculate distance between two points
       @author  kadamsagar039
       @version 3.7
        @since   24-12-2018"""


def start():
    start.startTimer = time.time()  # time() function return current time
    print("Start Time:", start.startTimer)  # hold start timing


def stop():
    stop.stopTimer = time.time()  # hold last timing
    print("Stop Time:", stop.stopTimer)


def elapsedTime():
    elapsed = stop.stopTimer - start.startTimer  # calculate elapsed time
    print()
    print("ElapsedTime:", elapsed)
    # print("Converting Milliseconds to Seconds",(elapsed/1000),"sec")


"""Purpose: WindChill
       @author  kadamsagar039
       @version 3.7
       @since   24-12-2018"""


def windChill(temp, windspeed):
    # check wind speed and temperature conditions
    if temp < 50 and 3 < windspeed < 120:

        # calculate windchill
        windchill = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(windspeed, 0.16)
        print()
        print("WindChill is", windchill)
    else:
        print("Enter Valid Input")

    # ********************************ALGORITHMS**********************************************

    # -----------------stringAnagram------------------------------

    """@author  kadamsagar039
       @version 3.7
       @since   26-12-2018"""


def checkAnagram(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):  # sort string and check equals or not
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # ----------------------isPrime Number-------------------------------

    """@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def isPrime(start, end):
    for val in range(start, end + 1):

        # If num is divisible by any number
        # between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:  # if condition satisfy then come out from loop
                    break
            else:
                # print(val)
                isPalindrome(val)

    # ----------------------isPalindrome-------------------------------

    """@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def isPalindrome(val):
    temp = val
    rev = 0  # Initialization
    while val > 0:
        rem = val % 10
        rev = rev * 10 + rem  # find reverse number
        val = val // 10
    if temp == rev:  # match with reversed number
        print("Palindrome number:")
        print(rev)  # print

    # ----------------------Question To Find Your Number-------------------------------

    """@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def question(low, high):
    if (high - low) == 1:  # if range is equal
        return low
    mid = int(high + low) / 2  # find middle value
    print('Is your number less than', mid, '?. press 1 to YES or 0 to NO:')
    a = int(input())
    if a == 1:
        return question(low, mid)  # recursive call for left half
    elif a == 0:
        return question(mid, high)  # recursive call for right half
    else:
        print("Invalid input.. ")
        return 0

    # ----------------------Vending machine-------------------------------

    """@author:  kadamsagar039
       @version: 3.7
       @since:  26-12-2018"""


def vendingMachine(money, notes):
    rem = 0
    while money > 0:  # if money is greater than zero
        for i in range(0, len(notes), 1):
            if money >= notes[i]:
                calNotes = money // notes[i]  # money divide by notes[i]
                rem = money % notes[i]
                money = rem  # remaining value assign to money
                total = int(calNotes)
                print(notes[i], " Notes ---> ", calNotes)
        vendingMachine(money, notes)  # recursive call
        print("Total no of notes:", total)

    # ----------------------Sorting Functions--------------------------------------------------------

    """@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


# ----------------------------Input Functions-------------------------------------------------


# To accept integer array
def inputIntList():
    N = int(input("Enter no of element:"))
    listArr = []
    for i in range(N):
        x = int(input("Enter element:"))
        listArr.append(x)  # add element one by one in list
    return listArr

    # To accept String array


def inputStringList():
    N = int(input("Enter no of element:"))
    listArr = []
    for i in range(N):
        x = input("Enter element:")
        listArr.append(x)  # add string values one by one in list
    return listArr


# -----------------------------BubbleSort----------------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def bubbleSort(listArr):
    temp = 0
    for i in range(0, len(listArr) - 1, 1):  # pass loop
        for j in range(1, len(listArr), 1):
            if listArr[j - 1] > listArr[j]:  # check previous element is greater or not
                temp = listArr[j - 1]  # If greater then swap each other
                listArr[j - 1] = listArr[j]
                listArr[j] = temp
    return listArr


# -----------------------------Binary Search----------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def binarySearch(arr, x):
    start = 0  # find start
    end = len(arr) - 1  # find end
    while start <= end:  # loop execute while start <= end
        mid = (start + end) // 2  # find mid
        if x == arr[mid]:  # if key match return mid which is key
            return mid

        if x < arr[mid]:  # if key less than mid value then change end
            end = mid - 1
        else:
            start = mid + 1  # if key greater than mid value then change start

    return -1  # if result not found then return -1

    # -------------------------------Insertion Sort---------------------------------------------------------
    """@author: kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def insertionSort(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]  # store value in currentValue which index at i
        pos = i  # i assign to position
        while pos > 0 and arr[pos - 1] > currentvalue:  # if pos > 0 and value of (pos-1) > current
            arr[pos] = arr[pos - 1]  # keep sorted list
            pos = pos - 1  # swapping
        arr[pos] = currentvalue  # keep as it is

    print(arr)


# -----------------------------------Merge Sort----------------------------------------------------
"""@author:  kadamsagar039
       @version: 3.7
       @since:   26-12-2018"""


def merge(left, right):
    result = []  # empty list
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    return merge(left, right)


# -----------------------------DayOfWeek----------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   27-12-2018"""


def dayOfWeek(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400  # find out day using formula's
    m0 = m + 12 * ((14 - m) // 12) - 2
    day = (d + x + 31 * m0 // 12) % 7

    # print day
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    else:
        print("invalid")


# -----------------------Temperature Conversion------------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   27-12-2018"""


def temperatureConversion(celsius, fahrenheit):
    celsiusTemp = (fahrenheit - 32) * 5 // 9  # fond temperature in celsius using formula
    print("Temperature in Celsius:", celsiusTemp)
    fahrenheitTemp = (celsius * 9 // 5) + 32  # fond temperature in fahrenheit usin formula
    print("Temperature in Fahrenheit:", fahrenheitTemp)


# -----------------------Monthly Payment------------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   27-12-2018"""


def monthlyPayment(p, y, r):
    n = 12 * y
    r0 = r / (12 * 100)
    pay = (p * r0) / (1 - math.pow(1 + r0, -n))
    print("Monthly payment is:", pay)


# ---------------------------SquareRoot--------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   27-12-2018"""


def sqrt(num):
    temp = num
    epsilon = 1e-15
    while math.fabs(temp - num / temp) > epsilon * temp:
        temp = ((num / temp + temp) / 2)
    print("SquareRoot is:", temp)


# ---------------------------ToBinary---------------------------------------------------

"""@author:  kadamsagar039
       @version: 3.7
       @since:   27-12-2018"""


def toBinary(str1):
    while len(str1) != 8:  # Padding the elements with 0
        str1 = "0" + str1
    print("Binary number after padding: ",str1)

    mid = len(str1) / 2
    part1 = str1[:int(mid)]  # Slicing start till mid
    part2 = str1[int(mid):]  # Slicing mid to end
    print("part 1:", part1)
    print("part 2:", part2)
    new_str = part2 + part1
    print("After Swap part1 and part2:", new_str)
    # int(bn, 2)
    new_no = (int(new_str, 2))      # type cast string to int
    print("New Number is", new_no)

    if isPowerOfTwo(new_no):  # Checking if its power of 2
        print("Its power of 2")
    else:
        print("Its not power of 2")


def logs(x):
    return math.log10(x) / math.log10(2)


def isPowerOfTwo(new_no):
    return math.ceil(logs(new_no)) == math.floor(logs(new_no))