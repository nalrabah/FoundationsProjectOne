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
cupcake_shop_name = "Sugar Rush"
signature_flavors = ["caramel apple","peppermint","blueberry","pumpkin spice","carrot cake"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print "There are " + str(len(menu)) + " items on the menu:"
    for key in menu:
      print "- %s: %s KD " % (key, menu[key]) 
# print_menu() ## How do I put coffee and tea next to each other?


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for cupcakes in original_flavors:
      print "- %s" % cupcakes
# print_originals()

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signature in signature_flavors:
        print  "- %s" % signature

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if (order in original_flavors) or (order in signature_flavors) or (order in menu): 
      return True
    else:
      return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order= raw_input("What would you like to order? (Enter the exact spelling of the item you would like to order. Type 'Exit' to end your order. \n")
    while order.lower() != "exit":
        if is_valid_order(order) == True:
            order_list.append(order)
            order = raw_input("What else? \n")
        elif is_valid_order(order) == False:
            order = raw_input("Please enter a valid order \n")
      # if order == "Exit":
      #   print("I am now breaking")
      #   break
      # order_list.append(order)

    print(order_list)
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if price > 4:
      print "Your order is eligible for credit card payment"
    else:
      print "Sorry! Your order is not eligible for credit card payment"

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in original_flavors:
            total+= original_price
        elif order in signature_flavors:
            total+= signature_price
        else:
            total+= menu[order]
    # your code goes here!

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print(order_list)
    total = get_total_price(order_list)
    print "Your total is %s KD. Thank you for shopping at Sugar Rush. Come back soon!" % total 
