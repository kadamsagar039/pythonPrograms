from object_oriented_utility.oops_util import StockReport


def stock_runner():
    try:
        stock = StockReport()
        stock.stock_report()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    stock_runner()