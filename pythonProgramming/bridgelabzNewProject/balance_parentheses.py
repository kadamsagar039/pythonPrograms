
"""Balanced Parentheses Program
This program is used to check whether user given arithmetic expression is balanced or not
Example:
    Balanced Expression :: {{a+b}*[a-b]}
    Unbalanced Expression:: {{a+b}*[a-b]
Author:
    Sagar <kadamsagar039@gmail.com>
Since:
    28 DEC,2018
"""

from ds_utilities.data_structure_util import Stack


def balance_parentheses():
    """
    This method is used as runner balanced_parentheses(string) method
    :return:  nothing
    """
    stack = Stack()
    try:
        string = input("Enter Expression to check for balanced Parentheses: ")
    except Exception as e:
        print(e)
        print("Enter String")

    stack.balanced_parentheses(string)


if __name__ == "__main__":
    balance_parentheses()