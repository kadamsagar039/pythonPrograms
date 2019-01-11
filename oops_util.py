import json
import re
import random
import datetime
import numpy as np
from ds_utilities.data_structure_util import Queue
from ds_utilities.data_structure_util import LinkedList
from ds_utilities.data_structure_util import Stack

li = LinkedList()


class Inventory:

    def __init__(self):
        pass

    # read data from JSON file
    with open("../object_oriented_utility/Inventory.json", "r") as jf:
        json_value = json.load(jf)     # load() convert file into python from json
        jf.close()                      # close file

    # Inventory class constructor
    def __init__(self, json_value, name=json_value["Rice"][0]["name"], weight=json_value["Rice"][0]["weight"],
                 price=json_value["Rice"][0]["price"]):
        self.existing_material = json_value     # Initialization of all members
        self.json_value = json_value
        self.name = name
        self.weight = weight
        self.price = price

        print("\n<--- Just Look at the Materials that We have in our Inventory and Select Accordingly --->\n")

    list_keys = []
    key_index = 0
    material_chosen = ''

    def inventory_materials(self):
        """This method display the all available inventories
        :return: this method not return anything

        """
        json_keys = self.json_value.keys()
        for key in json_keys:
            self.list_keys.append(key)      # append data into list
        for i in self.list_keys:
            print(self.key_index, i)        # print available inventory items one by one
            self.key_index += 1
        self.key_index = int(input("Enter"))    # Enter choice for required items
        self.material_chosen = self.list_keys[self.key_index]

    def see_category(self):
        """
                This method is used to display all items of inventory.
                and give chance to user for selecting items.
                :return:this method won't return
        """
        index = 0

        for i in self.json_value:

            if i == self.material_chosen:
                print("Now Look at the Category for ->", self.material_chosen, "<- that We have in our Inventory\n")

                for j in self.json_value[self.material_chosen]:
                    print(index, j)         # print all available inventory
                    index += 1              # increment index each time by 1

                index_update = index
                # this is optional if user don't find required item in inventory then
                # it helps to send request
                print(index_update, "If you did not find your match in our listed Category of ", self.material_chosen,
                    '\n Then Just add your required category of', self.material_chosen,
                    '\n  You will get it by Tomorrow\n')

                choice = int(input("Enter choice :"))   # take choice from user for particular item
                if index_update == choice:
                    self.update_category()          # after user activity update inventory using
                    return                          # update_category() method
                else:
                    price = self.json_value[self.material_chosen][choice]["price"]
                    self.set_price_per_kg(price)       # inventory price calculate
                    weight = int(input('Enter how many kilograms you want to buy'))
                    self.set_weight(weight)     # take weight from user
                    print('your total price is ')
                    print(self.get_price())        # it display all total price

    def update_category(self):
        """
            this method help to update category in inventory as per customer
            activities and requirements
            :param :nothing
            :return :nothing
        """

        user_requirement = str(input("Enter Your Requirement Now\n"))
        with open("../object_oriented_utility/Inventory.json", 'r') as jf:
            json_str = jf.read()        # read json file
            jf.close()
            json_value = json.loads(json_str)   # loads() convert json data into python data

        # this statement help to add user requirements in inventory
        with open("../object_oriented_utility/Inventory.json", 'w') as jf:
            json_value[self.material_chosen].append({"name": user_requirement,
                                                    "weight": 1,
                                                    "price": 50})

            jf.write(json.dumps(json_value))    # write data into json file
            jf.close()                  # close file

    def calculate(self):
        index = 0       # Initialization
        sum = 0
        for i in self.json_value:

            if i == self.material_chosen:           # select particular category
                for j in self.json_value[self.material_chosen]:
                    print(index, j)                 # print all items of that category
                    index += 1                      # increment index each time by one

                for k in range(index):
                    price = self.json_value[self.material_chosen][k]["price"]
                    sum = sum + price     # its calculate price of all items
        print("Total inventory amount is:", sum)        # print total amount

    # this method return name
    def get_name(self):
        return self.name

    # this method used to set name
    def set_name(self, value):
        self.name = value

    # this method return weight
    def get_weight(self):
        return self.weight

    # this method used to set weight
    def set_weight(self, weight):
        self.weight = weight

    # this method return price per kg
    def get_price_per_kg(self):
        return self.price

    # this method used to set price
    def set_price_per_kg(self, price):
        self.price = price

    # this method return overall price
    def get_price(self):
        price = self.get_price_per_kg() * self.get_weight()
        return price

# -----------------------------------------------------------------------------------------


class RegularExpression:

    def __init__(self):
        pass

    def regex(self):
        """
            This method take string and replace some part of string using regex methods.
            check for particular pattern and replace the string with user input.
            :param: Nothing
            :return: returns the string with proper replacement
        """

        string = 'Hello <<name>>, We have your full name as <<full name>> in our system.' \
                 '\n your contact number is 91-xxxxxxxxxx.' \
                 '\n Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2019. '
        # template list contain some patterns
        template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2019']
        # user input list
        list = ['Enter Your First Name: ', 'Enter Your Full Name: ', 'Enter Your Mobile Number(10 digits only):', "Enter Today's Date[dd/mm/yyy]:"]

        for i in range(4):
            print(' =>', list[i])   # print list array elements to take input from user
            # sub() method check the pattern and replace string with pattern
            replaced_string = re.sub(template[i], str(input()), string, 1)
            string = replaced_string

        return string      # return resultant string
# --------------------------------------------------------------------------------------------------------------


class StockReport:

    def stock_report(self):
        with open('../object_oriented_utility/Stock_Report.json', 'r') as jf:
            json_str = jf.read()            # read json file
            jf.close()
        json_value = json.loads(json_str)     # using loads() convert json data into python data
        count = 0
        for i in range(len(json_value['Stock Report'])):    # loop iterate till last element fo stock
            count1 = 1
            for key in (json_value['Stock Report'][i]):

                if i == 0 and count == 0:
                    for key1 in (json_value['Stock Report'][0]):
                        print(key1, end='\t')       # print keys element of json
                        count += 1
                        if count == len(json_value['Stock Report'][0]):
                            print(' Total Price ', end=' ')  # print total price at end

                    print()

                print(json_value['Stock Report'][i][key], end='\t\t\t')   # print company names
                if count1 == len(json_value['Stock Report'][i]):
                    # print data of stock report
                    print(json_value['Stock Report'][i]['Number of Share'] * json_value['Stock Report'][i]['Share Price'],
                        end='\t\t\t')
                count1 += 1         # increment counter by 1
            print()

# ------------------------------------------------------------------------------------------------


class Player:

    def shuffle(self):
        """
            This method shuffle the cards using Random method and then distribute 9
            Cards to 4 Players and Print the Cards the received by the 4 Players
            using 2D Array...
            :param : nothing
            :return: nothing
        """
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        list_cards = []

        while len(list_cards) < 36:
            for i in range(0, 9):
                random_no = random.randint(1, 13)   # it gives value between 1 to 13
                cards_rank = Rank[random_no - 1]     # pick random element from rank list
                random_no_suits = random.randint(0, 3)  # gives value between 0 to 3
                cards_rank = cards_rank + ' ' + suits[random_no_suits]
                if list_cards.__contains__(cards_rank) is False:  # check for repeated element
                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)   # if not contains by card_list then add it into list

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):
            for j in range(column):
                two_d_array[i][j] = list_cards[index]  # add cards into 2d array
                index += 1

        a = np.array(two_d_array)   # print 2d array
        print(a)


class Player1:

    def cards_queue(self):
        q = Queue()
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11 Jack", "12 Queen", "13 King", "14 Ace"]

        list_cards = []

        while len(list_cards) < 36:
            for i in range(0, 9):

                random_no = random.randint(1, 13)

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)
                cards_rank = cards_rank + ' ' + suits[random_no_suits]

                if list_cards.__contains__(cards_rank) is False:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):

            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1

        a = np.array(two_d_array)
        print(a)
        limit = 9
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for i in list_cards[0:9]:
            i = tuple((int(i[:2]), i[2:]))
            l1.append(i)
        l1.sort()
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in l1:
            q.enqueue(j)
        q.show()
        print()
        for i in list_cards[9:18]:
            i = tuple((int(i[:2]), i[2:]))
            l2.append(i)
        l2.sort()
        print("Player 2 Cards")
        for l in l2:
            q.enqueue(l)
        q.show()
        print()
        for i in list_cards[18:27]:
            i = tuple((int(i[:2]), i[2:]))
            l3.append(i)
        l3.sort()
        print("Player 3 Cards")
        for m in l3:
            q.enqueue(m)
        q.show()
        print()
        for i in list_cards[27:]:
            i = tuple((int(i[:2]), i[2:]))
            l4.append(i)

        l4.sort()
        print("Player 4 Cards")
        for n in l4:
            q.enqueue(n)
        q.show()
        return list_cards, two_d_array


# ------------------------------------------------------------------------------------------------


class Accounts:
    try:
        def __init__(self):
            with open("../object_oriented_utility/stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json
            self.stock_jf = stock_jf
            with open("../object_oriented_utility/customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)    # read customer json file
            self.person_json_value = person_json_value

        def view_shares(self):
            """
                This method display the all shares record
                :return: nothing
            """
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

        def check_validity(self):
            """
                This method provide user interface to customer as well as admin.
                It gives different options to sell and buy shares.
                :return: nothing
            """

            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username :")
            while i < len(self.person_json_value["Person"]):
                # title() method returns a copy of the string in which
                # first characters of all the words are capitalized.
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])  # print all data of customer
                    print("....Login successful....")

                    # provide options
                    c = int(input("1.Buy shares\n2.Sell shares\n3.Exit"))
                    if c == 1:
                        self.buy_share(index)       # for buying shares
                    elif c == 2:
                        self.sell_share(index)      # for selling shares
                    elif c == 3:
                        exit(0)
                    else:
                        # in case of user entered wrong input display following message
                        print("wrong Input")
                i += 1

        def add_new_company(self):
            """
                This method used to add new company into stock it can only
                done by admin.
                :return: nothing
            """
            name = input("Enter company name: ")
            number = int(input("Enter Number of share: "))
            price = int(input('Enter Price per share: '))
            new_stock_dict = {"Stock Name": name,               # add at new index in stock report
                              "Number of Share": number,
                              "Share Price": price}

            with open('../object_oriented_utility/stock.json', 'w') as stock_jf:
                self.stock_jf['Stock Report'].append(new_stock_dict)  # append updated data into stocks

                stock_jf.write(json.dumps(self.stock_jf, indent=2))

        def buy_share(self, index):
            """
                This method used to buy share from stocks its calculate the
                all stock price which is purchased by user.
            :param index:
            :return: nothing
            """
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])          # print stock data

            # taking input from user
            print('\nEnter Which Company Share you want to buy')
            choice = int(input("Enter company index number: "))
            buy_share = int(input("Enter Number of Share You want to buy: "))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            amount_pay = buy_share * each_share_price   # calculate total purchased share price

            # checks balance before purchase. if balance enough then proceed else terminate
            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                print("Total amount you have to pay for ", buy_share, " stocks :", amount_pay )
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share

                # update stocks after purchasing
                with open("../object_oriented_utility/stock.json", "w") as jf:
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                print('Now Your Updated Number of share is ', person_updated_share)

                # update customer data also
                with open("../object_oriented_utility/customers.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:

                # if customer don't have enough balance then print following message
                print("You Don't have enough money ")

        def sell_share(self, index):
            """
            This method used to sell share from customer stocks its calculate the
                all stock price which is sold by user.

            :param index:
            :return:nothing
            """

            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])  # print stock report

            choice = int(input("Enter choice (company index): "))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')
            sell_share = int(input("Number of shares to sell: "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share

            # update stock report data
            with open("../object_oriented_utility/stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))  # write updated data into stock report

            # calculate updated person shares
            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] + person_share_price * sell_share
            # print all transaction data
            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            # update customer data also
            with open("../object_oriented_utility/customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


# ----------------------------------------------------------------------------------------------------------------
s = Queue()
s1 = Queue()


class PersonQueue:
    try:
        def __init__(self):
            with open("../object_oriented_utility/stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("../object_oriented_utility/customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def view_shares(self):
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

        def check_validity(self):

            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username")
            while i < len(self.person_json_value["Person"]):
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        self.buy_share(index, name)
                    elif c == 2:
                        self.sell_share(index, name)

                    else:
                        print("wrong Input")


                i+=1

        def add_new_company(self):
            name = input("Enter company name")
            number = int(input("Enter Your Number of share"))
            price = int(input('Enter Your Price per share'))
            new_stock_dict = {"Stock Name": name,

                              "Number of Share": number,

                              "Share Price": price}

            with open('../object_oriented_utility/stock.json', 'w') as stock_jf:
                self.stock_jf['Stock Report'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))

        def buy_share(self, index, name):
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            print('Enter Which Company Share you want to buy')
            choice = int(input("Enter choice in Int"))
            buy_share = int(input("Enter Number of Share You want to buy"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            amount_pay = buy_share * each_share_price

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay )
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share
                with open("../object_oriented_utility/stock.json", "w") as jf:
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                print('Now Your Updated Number of share is ', person_updated_share)
                dt = datetime.datetime.now()

                s.push(("Buy", self.stock_jf["Stock Report"][choice]["Stock Name"],"Number of shares : ",buy_share))
                with open("../object_oriented_utility/transaction.txt", "a")as txt:
                    txt.write(name+str(s.show())+str(dt)+"\n")
                print("stack show")
                s.show()
                s1.enqueue("B")
                s1.show()
                with open("../object_oriented_utility/customers.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))

            else:
                print("You Don't have enough money ")

        def sell_share(self, index, name):
            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')
            sell_share = int(input("Number of shares to sell "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share
            with open("../object_oriented_utility/stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)
            st = datetime.datetime.now()

            s.enqueue(("Sold", self.stock_jf["Stock Report"][choice]["Stock Name"],"Number of shares : ",sell_share))
            with open("../object_oriented_utility/transaction.txt", "a")as txt:
                txt.write(name + str(s.show()) + str(st) + "\n")
            print("stack show")
            s.show()
            s1.enqueue("S")
            s1.show()
            with open("../object_oriented_utility/customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------------------------------

s = Stack()

s1 = Stack()


class Person:
    try:
        def __init__(self):
            with open("../object_oriented_utility/stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("../object_oriented_utility/customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def view_shares(self):
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

        def check_validity(self):

            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username")
            while i < len(self.person_json_value["Person"]):
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        self.buy_share(index, name)
                    elif c == 2:
                        self.sell_share(index, name)

                    else:
                        print("wrong Input")


                i+=1

        def add_new_company(self):
            name = input("Enter company name")
            number = int(input("Enter Your Number of share"))
            price = int(input('Enter Your Price per share'))
            new_stock_dict = {"Stock Name": name,

                              "Number of Share": number,

                              "Share Price": price}

            with open('../object_oriented_utility/stock.json', 'w') as stock_jf:
                self.stock_jf['Stock Report'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))

        def buy_share(self, index, name):
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            print('Enter Which Company Share you want to buy')
            choice = int(input("Enter choice in Int"))
            buy_share = int(input("Enter Number of Share You want to buy"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            amount_pay = buy_share * each_share_price

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay )
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share
                with open("stock.json", "w") as jf:
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                print('Now Your Updated Number of share is ', person_updated_share)
                dt = datetime.datetime.now()

                s.push(("Buy", self.stock_jf["Stock Report"][choice]["Stock Name"],"Number of shares : ",buy_share))
                with open("../object_oriented_utility/stack_transaction.txt", "a")as txt:
                    txt.write(name+str(s.show())+str(dt)+"\n")
                print("stack show")
                s.show()
                s1.push("B")
                s1.show()
                with open("../object_oriented_utility/customers.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))

            else:
                print("You Don't have enough money ")

        def sell_share(self, index, name):
            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')
            sell_share = int(input("Number of shares to sell "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share
            with open("../object_oriented_utility/stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)
            st = datetime.datetime.now()

            s.push(("Sold", self.stock_jf["Stock Report"][choice]["Stock Name"],"Number of shares : ",sell_share))
            with open("../object_oriented_utility/stack_transaction.txt", "a")as txt:
                txt.write(name + str(s.show()) + str(st) + "\n")
            print("stack show")
            s.show()
            s1.push("S")
            s1.show()
            with open("../object_oriented_utility/customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)
