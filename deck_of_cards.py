from object_oriented_utility.oops_util import Player


def deck_of_card():
    try:
        play = Player()
        play.shuffle()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deck_of_card()