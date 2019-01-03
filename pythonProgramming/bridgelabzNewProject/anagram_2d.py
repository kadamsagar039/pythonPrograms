"""Prime Anagram 2D array Program
In this program,prime number which are anagram will be stored in 2d array.
the prime number which are not anagram that should be stored below anagram in 2d array
Author:
    Sagar <kadamsagar039@gmail.com>
Since:
    02 JAN,2019
"""

from ds_utilities.data_structure_util import Logic


def anagram_2d_runner():
    """
    This method is act as runner for anagram_2d_array() method .
    :return: this will return nothing
    """
    logic_obj = Logic()
    logic_obj.anagram_2d_array()       # function call


if __name__ == "__main__":
    anagram_2d_runner()