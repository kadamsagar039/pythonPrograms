"""Calender using Queue Program
This program is used to take month and year from user and print corresponding Calender using queue

Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    31 DEC,2018
"""


from ds_utilities.data_structure_util import Logic


def calender_queue_runner():
    """
    This method act as runner for calender_queue(month, year) method
    :return:This method won't return anything
    """

    logic_obj = Logic()

    try:
        month = int(input('Enter Month:'))
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter year:'))
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calender_queue(month, year)


if __name__ == "__main__":
    calender_queue_runner()