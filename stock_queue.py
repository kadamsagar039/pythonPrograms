from object_oriented_utility.oops_util import PersonQueue


def queue_stock_runner():
    p = PersonQueue()
    p.view_shares()
    try:
        print("\n1.Admin login.\n2.User login.\n3.Exit ")
        choice = int(input("\nEnter choice:"))
        if choice == 1:
            print("\nwelcome Admin")
            print("\n1.To add Company\n2.Exit")
            j = int(input("Enter choice:"))
            if j == 1:
                p.add_new_company()
                p.view_shares()
            elif j == 2:
                exit(0)
            else:
                print("you have entered wrong input..")
        elif choice == 2:
            print("Welcome User")
            p.check_validity()
        elif choice == 3:
            exit(0)
        else:
            print("Invalid choice....")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queue_stock_runner()
