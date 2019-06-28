def enter_params():
    num_items = int(input("How many items, 0 to exit: "))
    if num_items == 0:
        return 0, 0, ""
    price_per_item = float(input("Price per item: "))
    state = str(input("State (UT, NV, TX, AL, CA): "))
    return num_items, price_per_item, state


def do_calculation(num_items, price, state):
    # discounts
    total = round(float(num_items * price), 2)

    if 0 < total < 1000.0:
        disc = 0.0
    elif 1000.0 <= total <= 5000.0:
        disc = 0.03
    elif 5000.0 <= total <= 7000.0:
        disc = 0.05
    elif 7000.0 <= total <= 10000.0:
        disc = 0.07
    elif 10000.0 <= total < 50000.0:
        disc = 0.10
    elif total >= 50000.0:
        disc = 0.15

    # taxes
    taxes = {"UT": 0.0685, "NV": 0.08, "TX": 0.0625, "AL": 0.04, "CA": 0.0825}

    base = total - round((total * disc), 2)
    final = base + round((base * taxes.get(state, 0)), 2)

    return final


def show_result(num_items, price, state):
    print("Num items: ", num_items)
    print("The price is: ", price)
    print("The state is: ", state)


def init():
    num_items = 1
    while num_items > 0:
        num_items, price_per_item, state = enter_params()
        if num_items == 0:
            break
        final = do_calculation(num_items, price_per_item, state)
        show_result(num_items, final, state)


if __name__ == "__main__":
    init()
