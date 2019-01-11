from ds_utilities.data_structure_util import LinkedList

import json


def linked_list_stock():
    l = LinkedList()
    with open('../object_oriented_utility/stock.json', "r") as f:
        f = json.load(f)

    for i in f["Stock Report"]:

        l.append(i)

    l.display()
    print("\n1.add stocks\n2.remove stocks\n3.exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print(l.display())
        comp_name = input("stock name")
        no_of_share = int(input("No of shares "))
        price_per_share = int(input("price per share : "))

        new_comp = {'Stock Name': comp_name,
                    'Number of Share': no_of_share,
                    'Share Price': price_per_share}
        l.append(new_comp)
        e = l.display()
        print(e)
    elif choice == 2:
        with open("../object_oriented_utility/stock.json", 'r') as jf:
            json_str = jf.read()        # read json file
            jf.close()
        json_value = json.loads(json_str)
        print(json_value)
        list3 = []
        data = input("Enter company name to remove: ")
        for i in range(len(json_value['Stock Report'])):
            for key in (json_value['Stock Report'][i]):
                list3.append(json_value['Stock Report'][i][key])
        print(list3)

        for i in (json_value['Stock Report']):
            for key in (json_value['Stock Report'][i]):
                if list3.__contains__(data):
                    l.remove(json_value['Stock Report'][i][key])
                    break
        e = l.display()
        print(e)

    elif choice == 3:
        exit(0)

    else:
        print("you have entered wrong input")
        exit(0)


if __name__ == "__main__":
    linked_list_stock()