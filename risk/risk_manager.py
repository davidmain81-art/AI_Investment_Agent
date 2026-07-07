def calculate_stop_loss(price, percent=3):
    stop_loss = price * (1 - percent / 100)
    return round(stop_loss, 2)


def calculate_take_profit(price, percent=10):
    take_profit = price * (1 + percent / 100)
    return round(take_profit, 2)