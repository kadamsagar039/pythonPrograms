"""Calender using Stack Program
This program is used to take month and year from user and print corresponding Calender using stack

Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    31 DEC,2018
"""

from ds_utilities.data_structure_util import Logic


def calender_stack_runner():
    """
    This method is used as runner for calender_stack(month, year) method
    :return:  nothing
    """

    logic_obj = Logic()

    try:
        month = int(input('Enter Month'))
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter Year'))
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calender_stack(month, year)


if __name__ == "__main__":
    calender_stack_runner()