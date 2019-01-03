""" Bank Cash Counter Program
This program actually demonstrate bank cash counter where people can come for withdraw money or
user can deposit money in the bank and from the beginning itself bank cash will be maintained accordingly

Author:
    Sagar<kadamsagar039@gmail.com>
Since:
    29 DEC,2018
"""

from ds_utilities.data_structure_util import Queue


def cash_counter():
    """
    This method is used to deposit or withdraw money from bank.
    :return: nothing
    """

    queue = Queue()
    bank_cash = 1000
    try:
        no_of_people = int(input('Enter Number of People in the Queue:'))
    except Exception as e:
        print(e)
        print("Enter no of people in integer only:")
    for i in range(0, no_of_people):
        queue.enqueue(i)

    print('Welcome To Mumbai Bank')
    for i in range(0, queue.size()):
        print('1.Deposit cash \n 2.Withdraw cash \n')
        choice = int(input("Enter choice:"))

        if choice == 1:

            try:
                deposit_amount = int(input("Enter Deposit Amount: "))
            except Exception as e:
                print(e)
                print("Enter amount in integer only..")
            bank_cash = bank_cash + deposit_amount
            queue.dequeue()

        if choice == 2:
            print()
            try:
                withdraw_amount = int(input("Enter How much cash you want to Withdraw:"))
            except Exception as e:
                print(e)
                print("Enter withdraw amount in integer only...")
            if withdraw_amount < bank_cash:
                bank_cash = bank_cash - withdraw_amount
                queue.dequeue()

            if withdraw_amount > bank_cash:
                print('Insufficient Fund in Bank')
                print('1. Kindly enter cash within ' + str(bank_cash) + ' range  \n 2.If you do not want and leave')
                withdraw_choice = int(input("Enter choice:"))

                if withdraw_choice == 1:
                    try:
                        withdraw_amount = int(input('Enter Withdraw Amount:'))
                    except:
                        print("Enter withdraw amount in integer only")
                    if withdraw_amount <= bank_cash:
                        bank_cash = bank_cash - withdraw_amount
                    queue.dequeue()

                if withdraw_choice == 2:
                    queue.dequeue()

        if i < queue.size():
            print('Next Person')

    print('Bank Balance => ' + str(bank_cash))


if __name__ == "__main__":
    cash_counter()


