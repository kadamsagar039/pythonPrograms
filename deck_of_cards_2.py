
from object_oriented_utility.oops_util import Player1


def deck_of_card():
    try:
        p = Player1()
        p.cards_queue()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deck_of_card()