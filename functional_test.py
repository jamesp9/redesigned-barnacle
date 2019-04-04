from random import randint
from timeit import default_timer

from stock_profit import get_max_profit

# (minute, price)
test_data = [
    (1, 10),
    (2, 7),
    (3, 5),
    (4, 8),
    (5, 11),
    (10, 9),
    (4, 8),
    (3, 6),
    (50, 5),
    (11, 5),
    (3, 11),
    (5, 5),
    (-5, 5),
]


def random_test_data(rows=100):
    """
    Generate random test data, with minute values potentially out of range
    """
    return [(randint(-3, 500), randint(9, 99)) for x in range(rows)]


if __name__ == '__main__':
    stock_prices_yesterday = random_test_data(100000)
    # stock_prices_yesterday = test_data

    start_time = default_timer()
    profit = get_max_profit(stock_prices_yesterday)
    print('Profit: {}'.format(profit))
    print('{} rows in {}'.format(len(stock_prices_yesterday),
                                 default_timer() - start_time))
