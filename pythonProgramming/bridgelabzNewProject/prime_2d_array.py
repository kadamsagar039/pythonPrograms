"""Prime Number stored in 2D array Program
This program is used to store prime numbers in two dimensional array.
Example:
    Like here prime number within 100 range will be stored in one dimension
    and next prime number within 100 to 200 range will be stored in  second dimension
    and so on.
Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    02 JAN,2018
"""

from ds_utilities.data_structure_util import Logic


def prime_2d_runner():
    """
    This method is act as runner for prime_number_2d_array() method.
    :return:nothing
    """
    logic_obj = Logic()
    logic_obj.prime_number_2d_array()


if __name__ == "__main__":
    prime_2d_runner()