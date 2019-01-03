"""
This program is used to generate number of possible binary search tree in
given number of test cases.

Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    31 DEC,2018
"""

from ds_utilities.data_structure_util import BinaryTreeNode


def binary_search_tree_runner():
    """
    This method act as runner for count_binary_search_tree(nodes_list) method
    :return: this won't return anything
    """
    binary_obj = BinaryTreeNode()
    try:
        nodes_count = int(input('Enter How many nodes you want to insert into list: '))
    except Exception as e:
        print(e)
        print("Enter Number of nodes in integer only")
    nodes_list = []
    print('Now Enter all test cases')
    for i in range(0, nodes_count):
        nodes_list.append(int(input("Enter:")))

    result = binary_obj.count_binary_search_tree(nodes_list)
    print("No of Binary tree possible in each test case is as follows")
    for i in result:
        print(i)


if __name__ == "__main__":
    binary_search_tree_runner()