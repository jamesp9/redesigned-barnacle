def remove_invalid_time_indices(minute_price_data):
    """
    Uses basis that time indice starts from 1 at 10am and trading happens
    for 8 hours (480 minutes).
    """
    invalid_count = 0
    for idx, row in enumerate(minute_price_data):
        if minute_price_data[idx][0] < 0 or minute_price_data[idx][0] > 480:
            minute_price_data.pop(idx)
            invalid_count += 1
    print('Removed {} invalid time indice(s)'.format(invalid_count))


def get_max_profit(minute_price_data):
    """
    minute_price_data: list of tuples of the form (minute, price)
    Could do with some memory optimisation once row count gets over a million.
    """

    remove_invalid_time_indices(minute_price_data)

    # Sort values by price
    sorted_data = sorted(minute_price_data, key=lambda row: row[1])

    min_price_minute, min_price = sorted_data[0]
    print('Min price: {}, {}'.format(min_price_minute, min_price))

    profit = 0
    # Work backwards from highest price, unil the buy before sell contidtion
    # with a one minute difference is met
    for idx in range(len(sorted_data)-1, -1, -1):
        max_price_minute, max_price = sorted_data[idx]

        if max_price_minute > (min_price_minute + 1):
            print('Max price: {} {}'.format(max_price_minute, max_price))
            profit = max_price - min_price
            break

    return profit
