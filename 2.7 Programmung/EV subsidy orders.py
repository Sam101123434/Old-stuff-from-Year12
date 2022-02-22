"""Runs the program for recording subsidy orders for electric vehicles."""
# Functions here


def int_input(prompt):
    """
    Take an integer input.

    This takes an input from the user until their put is a deciaml value.

    :param prompt:
    :return:
    """
    var = "word"
    while not var.isdigit():  # repeat until var is a decimal value
        var = input(prompt)
    return int(var)


def order_summary(completed_order):
    """
    Print out a summary of an order of EV subsidies.

    :param completed_order:
    :return:
    """
    print("Order Type: {}".format(ORDER_TYPES[completed_order[0]]))
    print("Name: {}".format(completed_order[1]))
    print("Phone Number: {}".format(completed_order[2]))
    if completed_order[0] == "e":  # if order is a promo event,
        # print out address as well
        print("Address: {}".format(completed_order[-1]))
    print("EVs ordered:")
    total_evs = 0
    for j in range(len(completed_order[3])):
        if completed_order[3][j] > 0:
            total_evs += completed_order[3][j]
            print("{} x {} @ ${} = {}".format(
                # prints number, type and total subsidy cost
                # of each kind of regular EV ordered
                completed_order[3][j],
                REGULAR[j], REGULAR_SUBSIDY,
                completed_order[3][j] * REGULAR_SUBSIDY))
    for j in range(len(completed_order[4])):
        if completed_order[4][j] > 0:
            total_evs += completed_order[4][j]
            print("{} x {} @ ${} = {}".format(
                # prints number, type and total subsidy cost
                # of each kind of top-rated EV ordered
                completed_order[4][j],
                TOP_RATED[j],
                TOP_RATED_SUBSIDY,
                completed_order[4][j] * TOP_RATED_SUBSIDY))
    print("Total EVs: {}".format(total_evs))
    print("Total Subsidy: ${}".format(completed_order[5]))
    if total_evs < MIN_EVS:
        # makes sure order contains valid amount of EVs
        print("ERROR___ - minimum 5 EVs required")
        return False  # ensures orders with less than minimum EVs are invalid
    else:
        return completed_order


def take_order():
    """
    Take an order of EV subsidies and return a collection of the order info.

    :return:
    """
    order = []
    print("Promo event or Phone call? ('e' or 'c')")
    order_type = ""  # collection of all order info
    while order_type not in ["e", "c"]:
        # ensures user is entering a valid option
        order_type = input("Order Type: ").lower()
        # ensures capitals also work
    order.append(order_type)
    name = ""
    while name == "":  # ensures user is entering a name
        name = input("Name: ")
        # no restrictions on name
    order.append(name)
    phone_number = int_input("Phone Number: ")
    order.append(phone_number)
    address = ""
    if order_type == "e":  # gets address if the order is a promo event
        while address == "":
            address = input("Address: ")
    print("======================== EVs ========================")
    subsidy = 0  # start with no subsidy
    print("Regular EVs\n-----------")
    regular_amount = []
    for regular_ev in REGULAR:
        # input amount of EVs for each model in regular
        amount = int_input("{} amount: ".format(regular_ev))
        subsidy += amount * REGULAR_SUBSIDY
        # add the subsidy cost for each EV onto the order
        regular_amount.append(amount)
    print("\nTop-rated EVs\n-------------")
    top_rated_amount = []
    for top_rated_ev in TOP_RATED:
        # input amount of EVs of each top-rated model
        amount = int_input("{} amount: ".format(top_rated_ev))
        subsidy += amount * TOP_RATED_SUBSIDY
        # add the subsidy cost for each EV onto the order
        top_rated_amount.append(amount)
    order.append(regular_amount)  # append order info into a collection
    order.append(top_rated_amount)
    order.append(subsidy)
    order.append(address)
    print("""---------------------------------------------
Order Summary
-------------""")
    final_order = order_summary(order)  # print order summary
    if final_order is not False:  # check if the order is valid
        proceed = ""  # give option to cancel order in case of a mistake
        while proceed not in ["y", "n"] and final_order is not False:
            proceed = input("Proceed with order?\n(y/n): ")
        if proceed == "y":
            return final_order
        else:
            return False  # return false order if order is cancelled
    else:
        return False  # return false order if order is invalid


# constants here
MIN_EVS = 5
ORDER_TYPES = {
    "e": "Promo Event",
    "c": "Phone Call"
}
REGULAR = [
    "Audi e-tron",
    "Volkswagen ID.4",
    "Kia Nero EV",
    "BMW i3",
    "Polestar 2",
    "Tesla Model Y Performance",
    "Jaguar I-PACE"
]
TOP_RATED = [
    "Tesla Model 3",
    "Hercules Alpha",
    "Ford Mustang Mach-E",
    "Volkswagen e-Golf",
    "Renault Zoe"
]
REGULAR_SUBSIDY = 2000
TOP_RATED_SUBSIDY = 5000


def main():
    """Run EV subsidy ordering program."""
    day_orders = []  # collection of orders for the day
    end = "n"
    while end == "n":  # loop while user wants to order
        day_order = take_order()
        if day_order is not False:
            # add order onto list of orders if it is valid
            day_orders.append(day_order)
        end = ""
        while end not in ["y", "n"]:
            # give option to exit for the day
            end = input("Done for the day?\n(y/n): ")
    print("""
Thank you for using this program.
==========================================
Registrations of Interest in EV Subsidy Received:
==========================================
    """)  # thank you message
    overall_subsidies = 0
    for i in range(len(day_orders)):
        # print out each order for that day
        print("Order {}:".format(i + 1))
        order_summary(day_orders[i])
        overall_subsidies += day_orders[i][5]
        print()
    print("Total orders: {}".format(len(day_orders)))
    print("Overall potential cost of orders: ${}".format(overall_subsidies))
    print("==========================================")


main()
