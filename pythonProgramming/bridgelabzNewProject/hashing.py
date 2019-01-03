"""Hashing Program
This program is used to store user data into hashtable efficiently using hash function
and user can search their data in O(1) time complexity and
if data is found then that data will be removed and saves into file
and if data is not found then that data will be added to the hashtable and saves into file
At last user can see the updated content of file
Author:
    Sagar<kadamsagar039@gmail.com>
Since:
       29 DEC 2018
"""

from ds_utilities.data_structure_util import HashTable


def hashing_runner():
    """
    This method acts as runner
    :return: nothing
    """

    hash_obj = HashTable()

    print('These are the Numbers in our File')
    file = open("/home/admin1/number.txt", "r")
    print(file.readline())
    try:
        number = int(input('Now enter the Number you are looking for: '))
    except Exception as e:
        print(e)
        print("Enter Number only")
    hash_obj.insert()
    print(hash_obj.search(number))

    print('Now Updated File Content are as Follows')
    hash_obj.file_update(number)


if __name__ == "__main__":
    hashing_runner()