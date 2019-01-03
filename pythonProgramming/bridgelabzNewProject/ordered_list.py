"""OrderedList File Program
This program is used to take input from file and user can see the content of file
then user can search for data that he is looking for .if the user data is found then
that data will be removed from  OrderedList and saves into file and vice versa
and at last user can see the updated content of file
Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    28 DEC,2018
"""

from ds_utilities.data_structure_util import OrderedList


def ordered_list():
    """
    This method is used to read content of file.
    this method also append data into orderedList to perform operation on it
    this method also acts as runner for various method
    :return:nothing
    """
    obj = OrderedList()
    list = []
    res = []
    file = open("/home/admin1/number.txt", "r+")

    list1 = file.readlines()

    file_string = list1[0]

    list1 = file_string.split()
    for i in range(0, len(list1)):
        list.append(list1[i].strip())
    file.close()
    res = [int(i) for i in list]
    res.sort()
    for j in list:
        obj.add(j)

    print("These are the data that we have in our File")
    print(res)

    try:
        data = str(input("Enter data you are looking for:"))
    except Exception as e:
        print(e)
        print("Enter string only")
    print(obj.search_item(data))

    print("The updated file content are as follows")
    obj.file_update(data)


if __name__ == '__main__':
    ordered_list()
