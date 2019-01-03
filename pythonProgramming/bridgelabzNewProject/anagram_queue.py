"""Prime Anagram using Queue Program
This program is used to find prime anagram within 0  to 1000 range and print through queue
Author:
    Sagar <kadamsagar039@gmail.com>
Since:
    02 JAN,2019
"""

from ds_utilities.data_structure_util import Logic


def anagram_runner():
    """
    This method act as runner for anagram_queue() method.
    :return: nothing
    """
    logic_obj = Logic()
    logic_obj.anagram_queue()


if __name__ == "__main__":
    anagram_runner()