"""Calender Program
This program is used to take month and year from user and print corresponding Calender

Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    31 DEC,2018
"""

from ds_utilities.data_structure_util import Logic


def calender_runner():
    """
    This method act as runner for calender_queue(month, year)
    :return: nothing
    """

    logic_obj = Logic()

    try:
        month = int(input('Enter month: '))
    except:
        print("Enter integer only ")

    try:
        year = int(input("Enter Year: "))
    except:
        print("Enter integer only")
    logic_obj.calender(month, year)


if __name__ == "__main__":
    calender_runner()
