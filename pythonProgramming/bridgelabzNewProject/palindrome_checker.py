"""Palindrome Checker Program
This program is used to check for palindrome.
here user can give their string to know whether
given string is palindrome or not
Example:
    Enter String to Check for Palindrome :: madam
    True
Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    29 DEC,2018
"""

from ds_utilities.data_structure_util import Deque


def palindrome_checker():
    """
    This method is used to check for palindrome .
    :return: this will return True if string is palindrome else return False
    """
    deque = Deque()
    try:
        string = input("Enter String to Check for Palindrome: ")
    except Exception as e:
        print(e)
    lower_string = string.lower()
    string = lower_string

    remove_space = ''
    for i in range(0, len(string)):
        if string[i] == ' ':
            continue

        remove_space += string[i]

    string = remove_space

    for i in string:
        deque.add_rear(i)
    reverse_string = ''
    for i in range(0, deque.size()):
        reverse_string += str(deque.remove_rear())

    if string == reverse_string:
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome_checker())