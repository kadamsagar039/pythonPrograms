from object_oriented_utility.oops_util import RegularExpression


def re_runner():
    try:
        obj = RegularExpression()
        print("The Modified String with user information are as follows")
        print(obj.regex())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    re_runner()