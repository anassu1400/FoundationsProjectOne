####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Cupcake Me!"
signature_flavors = ["white powder", "cold spice", "black cream"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for items in menu:
        print ("%s: %sKD" % (str(items), str(menu[items])))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for items in original_flavors:
        print ("%s" % (items))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for items in signature_flavors:
        print ("%s" % (items))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if (order in menu) or (order in signature_flavors) or (order in original_flavors):
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = input("Can you please enter your orders in the same spelling as shown in the menu(enter 'exit' to stop): ")
    while not (order == "exit"):
        if is_valid_order(order):
            order_list.append(order)
        order = input("and...")
    else:
        return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for i in order_list:
        if i in menu:
            total = total + menu[i]
        elif  i in signature_flavors:
            total = total + signature_price
            
        elif i in original_flavors:
            total = total + original_price
            
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print(order_list)
    print ("for the price of %s" % get_total_price(order_list))
    if accept_credit_card(get_total_price(order_list)):
        print ("you can use credit card")
    else:
        print ("you can't use credit card")

