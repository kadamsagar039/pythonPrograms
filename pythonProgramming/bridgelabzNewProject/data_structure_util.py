from Utilities import Utility


class Node:
    """
    This class is used to create Node
    """

    def __init__(self, data, next=None):
        """
        This is the constructor of Node class .
        :param data:user given value will be stored in this variable
        :param next: this variable keeps the address of next node
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    This class is used to create LinkedList
    """
    head = None

    def __init__(self):
        """
        This is constructor of LinkedList class
        """
        pass

    def append(self, data):
        """
        This method is used to append data given by user at the end of the LinkedList
        :param data:this value will be provided by user to append at the end of list
        :return: this method won't return anything
        """

        node = Node(data)  # creation of node

        if self.head is None:

            self.head = node  # if head is null then assign new node to head

        else:

            traverse = self.head

            while traverse.next is not None:  # else traverse pointer till last node and
                traverse = traverse.next  # append new node at end

            traverse.next = node

    def search_item(self, data):
        """
        This method is used to search data given by user.
        :param data:this is the data that user want to search in the list
        :return: this will return true if data is found else return False
        """

        traverse = self.head
        if self.head is None:  # execute if list empty
            return False

        while traverse.next is not None:
            if traverse.data == data:  # checks for matching data
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True  # for single node
        else:
            return False

    def remove(self, data):
        """
        This method is used to remove data from the Linked list specified by the user.
        :param data:specified by user which data to be removed
        :return:this will return None ,if LinkedList is Empty
        """
        traverse = self.head
        temp = self.head            # assignments of head
        if self.head is None:
            return None

        if traverse.data == data:
            self.head = traverse.next  # for first node of linked list
            return

        while traverse.next is not None:

            temp = traverse.next
            if temp.data == data:           # matching
                traverse.next = temp.next  # if data match with node then delete
                return

            traverse = traverse.next

    def display(self):
        """
        This method is used to display content of Linked list.
        this method return data present in each node of LinkedList
        and its also useful in HashTable to display each data stored
        in HashTable data structure
        :return:this will return each data in LinkedList
        """
        list = []
        traverse = self.head

        if self.head is None:
            return None  # if empty then return None

        while traverse.next is not None:
            list.append(traverse.data)  # append element in list till linked list not end
            traverse = traverse.next

        list.append(traverse.data)
        return list  # return Linked List

    def file_update(self, data):
        """
        This method is used to update file after any operation performed on LinkedList
        and it saves the data into the file.
        :param data: this is the data that is to be updated in file
        :return: nothing
        """
        file = open("/home/admin1/sagar.txt", "r+")
        file.truncate(0)
        file.close()
        if self.search_item(data) is True:      # search data using search method
            self.remove(data)                   # if found then remove

            file = open("/home/admin1/sagar.txt", "a+")
            linkedlist_content = []
            linkedlist_content = self.display()  # assign linked list to a list
            for i in linkedlist_content:
                file.write(i + " ", )  # write data into file
            file.close()

            file = open("/home/admin1/sagar.txt", "r")
            for i in file:
                print(i)  # print file
            file.close()
        else:
            self.append(data)  # if data not found then append data into file

            file = open("/home/admin1/sagar.txt", "a+")

            linkedlist_content = []
            linkedlist_content = self.display()

            for i in linkedlist_content:
                file.write(i + " ")  # write file data into list
            file.close()

            file = open("/home/admin1/sagar.txt", "r")
            for i in file:
                print(i)  # print list contents
            file.close()

# ----------------------------------------------------------------------------------------------------


class OrderedList:
    """
    This is used to create OrderedList.
    """
    head = None  # Initialize head as none

    def __init__(self):
        """
        This is the constructor of OrderedList class
        """
        pass

    def add(self, data):
        """
        This method is used to put data in OrderedList in increasing order.
        :param data: dat will be provided by user
        :return: nothing
        """
        node = Node(data)  # create node
        if self.head is None:  # if list is empty
            self.head = node  # assign node to head

        else:
            traverse = self.head
            if int(self.head.data) > int(node.data):  # compare data before adding it
                self.head = node  # for ascending order if head is greater
                node.next = traverse  # than given data then simply add it.

            if int(self.head.data) < int(node.data):  # if head of data less than new node of data
                temp = self.head
                while traverse.next is not None:
                    if traverse.data < node.data:
                        temp = traverse  # check where new node of data is less than
                    traverse = traverse.next  # next one and if condition satisfy then add

                if traverse.data < node.data:
                    temp = traverse

                temp1 = temp.next
                temp.next = node
                node.next = temp1

    def remove(self, data):
        """
        This method is used to remove data from the OrderedList specified by the user.
        :param data:specified by user which data to be removed
        :return:nothing
        """

        traverse = self.head
        temp = self.head
        if traverse.data == data:       # if element found at first position then
            self.head = traverse.next   # increment head and remove that element
            return

        while traverse.next is not None:

            temp = traverse.next
            if temp.data == data:           # search for matching element and remove it
                traverse.next = temp.next
                return

            traverse = traverse.next

    def search_item(self, data):
        """
        This method is used to search data given by user.
        :param data:this is the data that user want to search in the list
        :return: this will return true if data is found else return False
        """

        traverse = self.head
        while traverse.next is not None:

            if traverse.data == data:  # data matching
                    return True
            traverse = traverse.next
        if traverse.data == data:       # if found return true else return false
            return True
        else:
            return False

    def display(self):
        """
        This method is used to display content of OrderedList.
        this method return each data in each node in LinkedList
         and this method i created so that i can use in HashTable to display
         each data stored in HashTable data structure
        :return:this will return each data in OrderedList
        """
        list = []
        traverse = self.head

        if self.head is None:     # if list empty
            return

        while traverse.next is not None:
            list.append(traverse.data)  # append data into list
            traverse = traverse.next

        list.append(traverse.data)
        return list                     # return linked list

    def file_update(self, data):
        """
        This method is used to update file after any operation performed on OrderedList
        and it saves the data into the file.
        :param data: this is the data that is to be updated in file
        :return: nothing
        """
        file = open("/home/admin1/number.txt", "r+")
        file.truncate(0)
        file.close()

        if self.search_item(data) is True:              # if element found
            self.remove(data)                           # remove it using remove()
            file = open("/home/admin1/number.txt", "a+")

            orderedlist_content = []
            orderedlist_content = self.display()    # assign data to list return by
            for i in orderedlist_content:                   # display()  method
                file.write(i + " ", )                   # write data into file
            file.close()

            res = [int(i) for i in orderedlist_content]
            res.sort()      # sort linked list
            print(res)      # print linked list

        else:
            self.add(data)          # if data not found in list then add it

            file = open("/home/admin1/number.txt", "a+")

            orderedlist_content = []                            # assign data to list return by
            orderedlist_content = self.display()        # display() method
            for i in orderedlist_content:
                file.write(i + " ")                     # write data into file
            file.close()

            res = [int(i) for i in orderedlist_content]
            res.sort()          # sorting of element in ascending order
            print(res)          # print data of linked list


# -------------------------------------------------------------------------------------------------------


class Stack:
    """
    This is the Stack class to create Stack.
    """
    top = 0            # Initialization
    head = None

    def __init__(self):
        """
        This is the constructor of Stack class.
        """
        pass

    def push(self, data):
        """
        This method is used to insert data in stack.
        :param data:data will given by user
        :return: nothing
        """

        node = Node(data)       # create new node

        if self.head is None:

            self.head = node      # if head is empty then assign new node to head
        else:

            traverse = self.head

            while traverse.next is not None:    # else add to next null position
                traverse = traverse.next

            traverse.next = node

    def size(self):
        """
        This method is used to find the size of Stack.
        :return:this will return the size of stack
        """
        traverse = self.head

        if self.head is None:
            return 0
        size = 1
        while traverse.next is not None:    # traverse pointer till last node and
            traverse = traverse.next        # for each node size increment by 1
            size += 1
        return size                     # return count of element in the list

    def show(self):
        """
        This method is used to display content of stack.
        :return: nothing
        """
        traverse = self.head

        if self.top <= -1:      # print message if stack is underflow
            print(" Stack Underflow")
            return
        if traverse is None:
            print("Stack is empty")
            return

        while traverse.next is not None:
            print(traverse.data)        # print element of stack
            traverse = traverse.next
        print(traverse.data)

    def pop(self):
        """
        This method is used to delete last data which is inserted into the stack.
        actually stack follow the Last in First Out order to pop the data from the stack
        :return: this will return the data that will be removed
        """

        traverse = self.head

        if self.head is None:   # if stack empty return -1
            return -1

        if self.head.next is None:
            self.head = None           # if only one element in stack then

            return traverse.data        # set head as none and delete that element and return data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:             # else delete last node which is top on the stack
                traverse.next = None

                return t1.data
            traverse = traverse.next

    def peek(self):
        """
        This method is used to return the last inserted item in the stack.
        :return: return the last item inserted in the stack
        """
        traverse = self.head

        if self.head is None:
            return "empty stack"        # print if stack is empty
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next    # traverse pointer till last node

        return traverse.data            # return last node which is top element

    def is_empty(self):
        """
        This method is used to know wheter stack is empty or not.
        :return:this will return true if stack is empty else return False
        """

        if self.size() == 0:
            return True
        else:
            return False

    def balanced_parentheses(self, string):
        """
        This method is used to check whether expression is balanced or not.
        :param string: this is the expression which will be given by user
        :return: nothing
        """
        for i in string:

            if i == '(' or i == '[' or i == '{':
                stack.push(i)                       # adding element into stack

            if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
                    stack.peek() == '{' and i == '}')) and stack.size() > 0:
                stack.pop()
                continue

        if stack.size() == 0:
            print("Balanced Parenthesis ")      # after push and pop operation if stack size
        else:                                       # is zero then balanced otherwise unbalanced
            print("Parenthesis is not Balanced ")


stack = Stack()
stack1 = Stack()

# -----------------------------------------------------------------------------------------------------


class Queue:
    """
    This Queue class is used to create Queue.
    """
    front = None
    rear = None

    def __init__(self):
        """
        This is the constructor of Queue class .
        """
        pass

    def enqueue(self, data):
        """
        This method is used to insert data in the Queue .
        data will be given by user which data to be inserted ,
        queue follows First in First Out Principle.
        :param data: data will be given by user
        :return: nothing
        """

        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node       # front and rear assign to new node
            self.rear = node

        else:

            self.rear.next = node        # else add element in queue by rear
            self.rear = self.rear.next

    def show(self):
        """
        This method is used to display content of queue .
        :return: nothing
        """

        if self.front is None:
            print("Queue is empty")     # print if queue is empty
            return

        while self.front.next is not None:
            print(self.front.data)          # print queue data
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):
        """
        This method is used to delete data from the Queue.
        data will deleted according to FIFO principle
        :return: this will return the data that will be removed from the Queue
        """

        temp = self.front
        self.front = self.front.next        # delete data which is pointed by front pointer
        return temp.data                # return deleted data

    def is_empty(self):
        """
       This method is used to know whether Queue is empty or not.
       :return:this will return true if Queue is empty else return False
       """
        if self.front is None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to display content of queue.
        :return: nothing
        """

        size = 1
        traverse = self.front
        if self.front is None:      # return 0 if queue is empty
            return 0

        while traverse.next is not None:
            traverse = traverse.next        # traverse till last element and count size
            size += 1
        return size


queue = Queue()

# ----------------------------------------------------------------------------------------------------------------


class Deque:

    def __init__(self, front=None, rear=None):
        """
        This is the constructor of Deque class.
        :param front: this will always point to first node in the deque
        :param rear: this will always point to last node in the Deque
        """
        self.front = front
        self.rear = rear

    def add_front(self, data):
        """
        This method is used to insert data at front in Deque.
        :param data: data will be given by user that which data to be inserted in Deque
        :return: nothing
        """
        node = Node(data)
        if self.front is None and self.rear is None:
            self.front = node      # if front and rear == None
            # self.rear = node

        else:
            node.next = self.front     # add using front
            self.front = node

    def add_rear(self, data):
        """
        This method is used to insert data at last in Deque.
        :param data:data will be given by user
        :return: nothing
        """

        node = Node(data)

        if self.front == None and self.rear == None:

            # self.front = node
            self.rear = node

        else:

            self.rear.next = node       # add using rear
            self.rear = node

    def remove_front(self):
        """
        This is used to remove data which is at front in deque.
        :return:this will return the data which will be removed from the deque
        """

        if self.front.next is None:
            temp = self.front
            self.front = None       # if only one element in queue
            return temp.data

        temp = self.front
        self.front = self.front.next  # delete element of queue which is on front
        return temp.data

    def remove_rear(self):
        """       This is used to remove data which is at rear position in deque.
       :return:this will return the data which will be removed from the deque
       """

        traverse = self.front
        if self.rear == self.front:
            self.rear = None          # if queue contains only one element
            self.front = None
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next        # go till second last position

        rear_value = self.rear
        self.rear = traverse            # delete last element
        traverse.next = None
        return rear_value.data

    def is_empty(self):
        """
        This method is used to know whether Deque is empty or not.
        :return:this will return True if Deque is empty or else  return False.
        """

        if self.front is None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to calculate size of Deque
        :return: this will return size of Deque
        """

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:        # traverse till last element
            traverse = traverse.next
            size += 1
        return size                            # return size


# ------------------------------------------------------------------------------------------------------


class HashTable:
    """
    This HashTable class is used to create hashtable data structure.
    """

    def __init__(self):
        pass

    objects_list = []
    for i in range(11):
        """
        creating 11 objects of LinkedList class and storing it in list 
        that is in objects_list to make HashTable data structure
        """
        objects_list.append(LinkedList())

    def hash_function(self, key):
        """
        This method is used to convert users key or data into index.
        this index is used to store user data in hashtable on index which is obtained  by that particular
        data from hash_function
        :param key:data given by user as a key
        :return: this will return index for that data to store in hashtable
        """
        index = key % len(self.objects_list)
        return index

    def insert(self):
        """
        This method is used to read data from file and convert each data into
        integer format from string format.
        :return: nothing
        """

        file = open("/home/admin1/number.txt", "r")
        elements = file.readlines()     # read file data
        string = elements[0]

        string_list = string.split()       # split data using split() function

        elements = []
        for i in range(0, len(string_list)):
            to_integer = int(string_list[i])        # append data into list
            elements.append(to_integer)

        for i in range(len(elements)):
            index = self.hash_function(elements[i])         # append element at proper index
            self.objects_list[index].append(elements[i])

    def search(self, data):
        """
        This method is used to search data which is given by user in hashtable data structure.
        :param data:data will be given bu user
        :return: this will return true if data is found else return false
        """
        index = self.hash_function(data)
        return self.objects_list[index].search_item(data)

    def file_update(self, data):
        """
        This method is used to update file after any operation happened in hashtable
        data structure.
        :param data:this is the data that is to be removed or added to the file according to search result
        :return: nothing
        """
        result = self.search(data)

        if result is True:
            index = self.hash_function(data)
            self.objects_list[index].remove(data)     # if data found then remove it
            self.display_content_hashtable()

        if result is False:
            index = self.hash_function(data)
            self.objects_list[index].append(data)    # if data not fount add it into list
            self.display_content_hashtable()

    def display_content_hashtable(self):
        """
        This method is used to display content of HashTable data structure.
        :return:nothing
        """

        file = open("/home/admin1/number.txt", "r+")
        file.truncate(0)
        file.close()
        for i in range(0, len(self.objects_list)):

            if self.objects_list[i].display() is not None:
                lines = []
                lines = self.objects_list[i].display()      # add element into list which returned
                file = open("/home/admin1/number.txt", "a+")   # by display function
                for j in lines:
                    file.write(str(j) + ' ')

        file.close()

        file = open("/home/admin1/number.txt", "r")
        for i in file:
            print(i)
        file.close()
# ---------------------------------------------------------------------------------------------------


class BinaryTreeNode:

    def __init__(self):
        pass

    def binary_search_tree(self, test_cases):
        """
        This method is used to calculate possible number of binary search tree in given number of node.
        using catlan number formula= ((2n)! / ((n+1)! * n!))
        :param test_cases:No of node given by user
        :return: this will return the number of binary search tree possible
        """
        number_of_bst = []
        for n in test_cases:
            fact1 = 1
            for m in range(1, (n * 2) + 1):  # find factorial (2n)!
                fact1 = fact1 * m

            fact2 = 1
            num = n + 1
            for l in range(1, num + 1):         # find factorial (n+1)!
                fact2 = fact2 * l

            nfact = 1

            for k in range(1, n + 1):     # find factorial (n!)
                nfact = nfact * k
        # using catalan number formula we can get output
            number_of_bst.append((fact1 // (fact2 * nfact)) % 100000007)
        return number_of_bst

# ----------------------------------------------------------------------------------------------------------------


class Methods:
    """
    This class Methods is used to write logics of various programs.
    """

    def __init__(self):
        pass

    def anagram_stack(self):
        """
        This method is used to print prime anagram in reverse order.
        :return: nothing
        """
        for i in Utility.get_anagram_prime():   # get anagram numbers which are prime
            stack.push(i)                         # push numbers into stack

        for i in range(0, stack.size()):
            print(stack.pop())                  # print in reverse order

    def anagram_queue(self):
        """
        This method is used to print prime anagram using queue.
        :return:
        """

        for i in Utility.get_anagram_prime():    # get anagram numbers which are prime
            queue.enqueue(i)                     # add numbers into queue

        for i in range(0, queue.size()):
            print(queue.dequeue())                 # print in reverse order

    def prime_number_2d_array(self):
        """
        This method is used to store prime number in matrix or 2d array
        and print in proper order.
        :return: nothing
        """

        prime_list = Utility.get_prime()  # get prime number
        row = 10
        column = 25
        limit = 100
        # create empty 2d array
        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0
        for i in range(row):

            for j in range(column):

                if k < len(prime_list):
                    if prime_list[k] <= limit:              # prime number check with the limit
                        two_d_array[i][j] = prime_list[k]   # add number into array
                        k += 1

            limit += 100            # increment limit by 100 for each iteration

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")   # display elements in 2d array format

            print()

    def anagram_2d_array(self):
        """
        This method is used to store prime anagram and prime number which are not anagram in matrix or 2d array.
        and print them accordingly
        :return:nothing
        """
        prime_list = Utility.get_prime()            # get prime numbers
        anagram_list = Utility.get_anagram_prime()  # get anagram numbers which is prime also
        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]
        k = 0
        index = 0
        for i in prime_list:
            if anagram_list.__contains__(i) is not True:     # if file not contains same element
                not_anagram.append(i)                       # append into not_anagram list

        for i in range(row):

            for j in range(column):

                if k < len(anagram_list):
                    two_d_array[i][j] = anagram_list[k]     # add element of anagram list into array
                    k += 1

                if k >= len(anagram_list) and index < len(not_anagram):
                    two_d_array[i][j] = not_anagram[index]     # add element of not_anagram list
                    k += 1                                      # into same array after anagram_list
                    index += 1
        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")  # print 2d array

            print()

    def calender(self, month, year):
        """
        This method is used to print Calender of given month and year.
        :param month: month given by user
        :param year: year given by user
        :return: nothing
        """

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        print(d0)
        if Utility.isleap_year(str(year)):      # check leap year
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # create empty 2d array

        print('Your Calender is\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')     # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:           # while d0 is less than j
                        two_d_array[i][j] = ' '      # it will print blank space
                        continue

                    two_d_array[i][j] = values       # add days into calender
                    values += 1                       # increment counter

        for i in range(row):

            for j in range(column):
                if two_d_array[i][j] != 0:
                    x = two_d_array[i][j]     # ljust() method returns the string
                    x1 = str(x).ljust(2)      # left justified in a string of length width.
                    print(x1, end=" ")

            print()

    def calender_queue(self, month, year):

        """
        This method is used to print calender of given month and year.
        In this method calender is created using queue
        :param month:month given ser
        :param year: year given by year
        :return: nothing
        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if Utility.isleap_year(str(year)):     # check leap year
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')       # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:       # while d0 is less than j
                    if i == 0 and j < d0:       # it will print blank space
                        queue.enqueue(' ')      # used enqueue() method of queue class
                        continue                # to add space

                    queue.enqueue(values)       # add element in queue
                    values += 1

        for i in range(row):

            for j in range(column):
                if queue.size() > 0:
                    x = queue.dequeue()    # remove element from queue and store it in x variable
                    x1 = str(x).ljust(2)    # using ljust() method print formated calender
                    print(x1, end=" ")
            print()

    def calender_stack(self, month, year):
        """
        This method is used to print calender of given month and year.
        In this method calender is created using stack
        :param month:month given ser
        :param year: year given by year
        :return: nothing
        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if Utility.isleap_year(str(year)):         # check leap year
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')              # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:        # while d0 is less than j
                    if i == 0 and j < d0:        # it will print blank space
                        stack.push(' ')          # use push() to add blanks
                        continue

                    stack.push(values)           # add days using push() method
                    values += 1

        for i in range(stack.size()):
            stack_element = stack.pop()         # pop element from stack and store in local variable
            stack1.push(stack_element)          # again push element into stack for reverse

        for i in range(row):

            for j in range(column):
                if stack1.size() > 0:
                    x = stack1.pop()          # access element one by one using pop() method
                    x1 = str(x).ljust(2)       # ljust() method to print in calender structure
                    print(x1, end=" ")

            print()
