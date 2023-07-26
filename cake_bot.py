import random
from random import randint
import sys

# bugs - prints delivery above cake menu

# constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

# list of random names
names = ["Nadia","Alissa","Courtney","Mia","Emma","Jasper","Loui","Harry","Joe","Zachary"]
# list of cake names
cake_names = ['Vanilla Cake','Chocolate Cake','Strawberry Cake','Caramel Cake',
              'Red Velvet Cake','Carrot Cake','Lemon Cake' ,'Ice Cream Cake',
              'Vanilla Mousse Cake','Chocolate Mousse Cake','Black Forest Cake','Blueberry Cake']
# list of cake prices
cake_prices = [35, 35, 39.90, 39.90, 39.90, 39.90,
               39.90, 39.90, 39.90, 45, 49.90, 49.90]
# list to store order list
order_list = []
# list to store order cost 
order_cost = []

# customer details dictionary
customer_details = {}

# validates input to check if they are an integer 
def val_int(low,high,question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"The number must be between {low} and {high} ")
        except ValueError:
            print("This is not a valid number")
            print(f"The number must be between {low} and {high} ")

# validates input to check if they are alphabetical
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters")
        else: 
            return response.title()

# validates input to check if left blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank ")

# validates phone number
def check_phone(question,PH_LOW,PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0 
            while test_num > 0: 
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number ")

# welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("== Welcome to Cloud Cakes ==")
    print("== My name is", name," ==")
    print("== I will be assisting you in picking cakes today! ==")

# menu for click and collect or delivery
def order_type():
    del_pick = ""
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    print("Do you want your cake to be delivered, or will you be picking it up?")
    print("For delivery, please enter 1")
    print("For click and collect, please enter 2")
    delivery = val_int(LOW,HIGH,question)
    if delivery == 1:
        print()
        print("Delivery")
        print()
        del_pick = "delivery"
        delivery_info()
    elif delivery == 2:
        print()
        print("Click and Collect")
        print()
        del_pick = "click and collect"
        clickandcollect_info()

    return del_pick

# delivery information - name, address, and phone number
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question,PH_LOW,PH_HIGH )
    print(customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question )
    print(customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = check_string(question)
    print(customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = check_string(question)
    print(customer_details['suburb'])

# click and collect information - name and phone number
def clickandcollect_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question,PH_LOW,PH_HIGH)
    print(customer_details['phone'])

def menu():
    number_cakes = 12
    for count in range (number_cakes):
        print("{} {} ${:.2f}" .format(count+1,cake_names[count],cake_prices[count]))

# choose total number of cakes - max 12
def order_cake():
    # ask for total number of cakes for order
    print()
    print("There is a maximum limit of 12 cakes per order.")
    num_cakes = 0
    NUM_LOW = 1
    NUM_HIGH = 12
    question = (f"Please enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many cakes would you like to order? ")
    num_cakes = val_int(NUM_LOW,NUM_HIGH,question)
    # choose cake from menu
    for item in range(num_cakes):
        while num_cakes > 0:
            print()
            print("Please choose your cakes from the menu above ")
            question = (f"Please enter a number between {NUM_LOW} and {NUM_HIGH} ")
            cakes_ordered = val_int(NUM_LOW,NUM_HIGH,question)

            cakes_ordered = cakes_ordered-1
            order_list.append(cake_names[cakes_ordered])
            order_cost.append(cake_prices[cakes_ordered])
            print("{} ${:.2f}" .format(cake_names[cakes_ordered],cake_prices[cakes_ordered]))
            num_cakes = num_cakes-1

# print order - including if order is for del or click and collect
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "delivery":
        print("Your order is for Delivery.")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    elif del_pick == "click and collect":
        print("Your order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    if del_pick == "delivery":
        if len(order_list) >= 5:
            print("As you have ordered 5 or more cakes, your order will be delivered for free.")
        elif len(order_list) < 5:
            print("As you have ordered less than 5 cakes, you will be charged a $9.00 delivery fee.")
            total_cost = total_cost + 9
    print()
    print("Total Order Cost")
    print(f"The total cost of the order is: ${total_cost:.2f}")
    print()

# ability to confirm or cancel order
def confirm_cancel():
    question = (f"Pleaes enter a number between {LOW} and {HIGH} ")
    print("Please confirm your order")
    print("To confirm, please enter 1")
    print("To cancel , please enter 2")
    confirm = val_int(LOW,HIGH,question)
    if confirm == 1: 
        print()
        print("Order confirmed")
        print("Your order has been sent to our bakery")
        print("Your cake(s) will be with you shortly")
        new_exit()
    elif confirm == 2: 
        print()
        print("Your order has been cancelled")
        print("You can restart your order or exit the BOT")
        new_exit()

# option for new order or exit BOT
def new_exit():
    print()
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    print("Would you like to make another order or exit?")
    print("To make another order, please enter 1")
    print("To exit the BOT, please enter 2")
    confirm = val_int(LOW,HIGH,question)
    if confirm == 1:
        print()
        print("New Order")
        print()
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
    elif confirm == 2:
        print()
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit
   
def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    welcome()
    del_pick = order_type()
    print(del_pick)
    menu()
    order_cake()
    print_order(del_pick)
    confirm_cancel()


    


main()



