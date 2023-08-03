# Cake Bot
# A program used to order cakes from a bakery


# modules
import random
# imports random module for generating variables
from random import randint
# variables are random integers
import sys
# imports system module to provide functions and variables


# constants
LOW = 1  # universal variable, sets constant LOW = 1
# constant used in order type, confirm or cancel order,
# and start another order or exit bot
HIGH = 2  # universal variable, sets constant HIGH = 2
# constant used in order type, confirm or cancel order,
# and start another order or exit bot
PH_LOW = 7  # sets minimum digits to input for standard NZ phone number
# constant used in phone number
PH_HIGH = 10  # sets maximum digits to input for standard NZ phone number
# constant used in phone number

# list of random names
names = ["Nadia", "Alissa", "Courtney", "Mia", "Emma",
         "Jasper", "Loui", "Harry", "Joe", "Zachary"]
# list of cake names
# these are the types of cake sold at the bakery
cake_names = ['Vanilla Cake', 'Chocolate Cake', 'Strawberry Cake', 'Caramel Cake',
              'Red Velvet Cake', 'Carrot Cake', 'Lemon Cake', 'Ice Cream Cake',
              'Vanilla Mousse Cake', 'Chocolate Mousse Cake', 'Black Forest Cake', 'Blueberry Cake']
# list of cake prices
# these are the prices of the cakes sold at the bakery
cake_prices = [35, 35, 39.90, 39.90, 39.90, 39.90,
               39.90, 39.90, 39.90, 45, 49.90, 49.90]
# list to store cakes ordered
# stores order for program to append the names of all cakes ordered
order_list = []
# list to store cost of cakes ordered
# stores order for program to append the cost of all cakes ordered
order_cost = []

# customer details dictionary
# a list to store the customer's information from input
customer_details = {}


# defines function as val_int
# validates input to check if they are an integer


def val_int(LOW, HIGH, question):
    # takes constants LOW and HIGH as parameters
    # also takes question as parameter
    # returns input if integer is valid
    while True:
        # sets up while loop
        try:
            # the program will print the statement
            num = int(input(question))  # asks for input (integer)
            if num >= LOW and num <= HIGH:
                # if num is equal to or in between num boundaries
                # return num
                return num
            else:
                # if num is outside num boundaries
                # prints error message
                print(f"The number must be between {LOW} and {HIGH} ")
        except ValueError:
            # if the input is not an integer
            # except code will print error message
            # and ask for input again
            print("This is not a valid number")
            # prints error message statement
            print(f"The number must be between {LOW} and {HIGH} ")
            # prints instruction statement


# defines function as check_string
# validates input to check if they are a string


def check_string(question):
    # takes question as parameter
    # returns response in title class if valid
    while True:
        # sets up while loop
        # asks for input (string)
        response = input(question)
        # checks that input is alphabetical
        x = response.isalpha()
        if x == False:
            # if response is not a string
            # prints error message
            print("Input must only contain letters")
        else:
            # returns input in title class
            return response.title()


# defines function as not_blank
# validates input to make sure it is not left blank


def not_blank(question):
    # takes question as parameter
    # returns reponse in title class if valid
    valid = False
    while not valid:
        # sets up while loop
        # asks user for input
        response = input(question)
        if response != "":
            # returns reponse to title class if input is valid
            # breaks the loop
            return response.title()
        else:
            # prints error message if input is blank
            print("This cannot be blank ")


# defines function as check_phone
# validates phone number


def check_phone(question, PH_LOW, PH_HIGH):
    # takes constants PH_LOW and PH_HIGH as parameters
    # also takes question as parameter
    # returns num if input is valid
    while True:
        # sets up while loop
        try:
            # asks for phone number input (integer)
            num = int(input(question))
            test_num = num
            # sets count to 0
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            # checks that input is within boundaries PH_LOW and PH_HIGH
            if count >= PH_LOW and count <= PH_HIGH:
                # returns num if input is valid within boundaries
                return num
            else:
                # prints error message if input is out of boundary range
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            # except error prints error message if input is not valid integer
            print("Input must only contain numbers ")

# defines welcome function
# function that welcomes the customer to bot


def welcome():
    '''
    Purpose: Generates a random name from the list and print out a welcome message
    Parameters: None
    Returns: None
    '''
    # allows bot to take a random name from list of names
    num = randint(0, 9)
    name = (names[num])
    # prints welcome message
    print("== Welcome to Cloud Cakes ==")
    # prints out randomly selected name from list
    print("== My name is", name, " ==")
    print("== I will be assisting you in picking cakes today! ==")
    print()  # prints blank space

# defines function order_type
# asks the user if cake is for delivery or click and collect


def order_type():
    # takes constants LOW and HIGH as parameters
    # also takes question as parameter
    # returns del_pick if input is valid
    del_pick = ""  # defines del_pick as a variable
    # defines the question
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    print("How would you like to receive your cake?")
    # prints instructions
    print("For delivery, please enter 1")
    print("For click and collect, please enter 2")
    print()  # prints blank space
    # asks for valid input (integer) within boundaries
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print()  # prints blank space
        # prints the option that the user selected
        print("Selected Delivery")
        print()  # prints blank space
        # sets order type variable to delivery
        del_pick = "delivery"
        # calls function delivery_info
        delivery_info()
    elif delivery == 2:
        print()  # prints blank space
        # prints the option that the user selected
        print("Selected Click and Collect")
        print()  # prints blank space
        # sets order type variable to click and collect
        del_pick = "click and collect"
        # calls function clickandcollect_info
        clickandcollect_info()

    # returns del_pick if input is valid
    return del_pick

# defines function as delivery_info
# collects the user's delivery information - name, address, and phone number


def delivery_info():
    # takes constansts PH_LOW and PH_HIGH as parameters
    # also takes question as parameter
    # no returns

    # asks for user's name to store in customer_details dictionary
    # information is stored under 'name'
    # defines question
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    # prints customer's name
    print(customer_details['name'])

    # asks for user's phone number to store in customer_details dictionary
    # information is stored under 'phone'
    # defines question
    question = ("Please enter your phone number ")
    # asks for input
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # prints customer's phone number
    print(customer_details['phone'])

    # asks for user's house number to store in customer_details dictionary
    # information is stored under 'house'
    # defines question
    question = ("Please enter your house number ")
    # asks for input
    customer_details['house'] = not_blank(question)
    # prints customer's house number
    print(customer_details['house'])

    # asks for user's street name to store in customer_details dictionary
    # information is stored under 'street'
    # defines question
    question = ("Please enter your street name ")
    # asks for input
    customer_details['street'] = check_string(question)
    # prints customer's street name
    print(customer_details['street'])

    # asks for user's suburb to store in customer_details dictionary
    # information is stored under 'suburb'
    # defines question
    question = ("Please enter your suburb ")
    # asks for input
    customer_details['suburb'] = check_string(question)
    # prints customer's suburb
    print(customer_details['suburb'])
    print()  # prints blank space

# defines function as clickandcollect_info
# collects the user's click and collect information - name and phone number


def clickandcollect_info():
    # takes constants PH_LOW and PH_HIGH as parameters
    # also takes question as parameter
    # no returns

    # asks for user's name to store in customer_details dictionary
    # information is stored under 'name'
    # defines question
    question = ("Please enter your name ")
    # asks for input
    customer_details['name'] = check_string(question)
    # information is stored under 'name'
    print(customer_details['name'])

    # asks for user's phone number to store in customer_details dictionary
    # information is stored under 'phone'
    # defines question
    question = ("Please enter your phone number ")
    # asks for input
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # information is stored under 'phone'
    print(customer_details['phone'])
    print()  # prints blank space

# defines function as menu
# a menu containing the 12 types of cake sold


def menu():
    # total number of cakes
    number_cakes = 12
    for count in range(number_cakes):
        # format prints the index number, cake name, and price of the cake
        # price is formatted to include 2 decimal places
        # index number starts at 1 when count+1
        print("{} {} ${:.2f}" .format(
            count+1, cake_names[count], cake_prices[count]))


# defines function as order_cake
# allows the user to choose how many cakes for order
# also allows user to pick cakes from menu

def order_cake():
    print()  # prints blank space
    # prints statement to let user know about the boundary
    print("There is a maximum limit of 12 cakes per order.")
    # num_cakes variable is set to 0
    num_cakes = 0
    # new constants set for function
    NUM_LOW = 1
    NUM_HIGH = 12
    # choosing how many cakes for order
    # defines question
    question = (f"Please enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many cakes would you like to order? ")
    # asks user for input (integer)
    num_cakes = val_int(NUM_LOW, NUM_HIGH, question)
    # choosing cakes from the menu
    # sets range to repeat action until loop is finished
    for item in range(num_cakes):
        while num_cakes > 0:
            # sets while loop until order is finished, or until num_cakes = 0
            print()  # prints blank space
            print("Please choose your cake(s) from the menu above ")
            question = (
                f"Please enter a number between {NUM_LOW} and {NUM_HIGH} ")
            # asks the user for input (integer)
            cakes_ordered = val_int(NUM_LOW, NUM_HIGH, question)

            # organises cake index to match list index
            cakes_ordered = cakes_ordered-1
            # appends the selected cake to order list
            order_list.append(cake_names[cakes_ordered])
            # appends the selected cake to order list
            order_cost.append(cake_prices[cakes_ordered])
            # prints the cake ordered with corresponding price
            # formatted to print cake name and price with 2 decimal places
            print("{} ${:.2f}" .format(
                cake_names[cakes_ordered], cake_prices[cakes_ordered]))
            # decreases nuber of cakes in variable for every input
            num_cakes = num_cakes-1

# defines function as print_order
# prints the order details - customer details, cakes ordered, and cost details


def print_order(del_pick):
    # takes del_pick as parameters
    # no returns
    print()  # prints blank space
    # calculates the total cost of all cakes ordered
    total_cost = sum(order_cost)
    # prints a header for customer details
    print("Customer Details")
    if del_pick == "delivery":
        # prints del_pick variable from order_type function
        print("Your order is for Delivery.")
        # prints customer's name, phone number, and address for delivery
        print(
            f"Customer Name: {customer_details['name']} \
             \nCustomer Phone: {customer_details['phone']} \
             \nCustomer Address: {customer_details['house']} \
             {customer_details['street']} {customer_details['suburb']}")
    elif del_pick == "click and collect":
        # prints del_pick variable from order_type function
        print("Your order is for Click and Collect")
        # prints customer's name and phone address for click and collect
        print(
            f"Customer Name: {customer_details['name']} \
                \nCustomer Phone: {customer_details['phone']}")
    print()  # prints blank space
    # prints heading for order details
    print("Order Details")
    # sets count variable to 0
    count = 0
    for item in order_list:
        # prints ordered cakes with respective prices
        # price is formatted to 2 decimal places
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        # starts count at 1
        count = count+1
    print()  # prints blank space
    if del_pick == "delivery":
        # if there are 5 or more items stored in order_list
        if len(order_list) >= 5:
            # prints statement
            print(
                "As you have ordered 5 or more cakes, your order will be delivered for free.")
        # if there are less than 5 items stored in order_list
        elif len(order_list) < 5:
            # prints statement
            print(
                "As you have ordered less than 5 cakes, you will be charged a $9.00 delivery fee.")
            # adds a $9 delivery charge to total cost
            total_cost = total_cost + 9
    print()  # prints blank space
    # prints heading for total order cost
    print("Total Order Cost")
    # prints the total cost of order and formats it to 2 decimal places
    print(f"The total cost of the order is: ${total_cost:.2f}")
    print()  # prints blank space


# defines function as confirm_cancel
# allows user to confirm or cancel order


def confirm_cancel():
    # takes constants LOW and HIGH as parameters
    # also takes question as parameter
    # no returns
    question = (f"Pleaes enter a number between {LOW} and {HIGH} ")
    print("Please confirm your order")
    print("To confirm, please enter 1")
    print("To cancel , please enter 2")
    # asks user for input (integer)
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print()  # prints blank space
        # prints statement confirming order
        print("Order confirmed")
        print("Your order has been sent to our bakery")
        print("Your cake(s) will be with you shortly")
        # proceeds to next function
        new_exit()
    elif confirm == 2:
        print()  # prints blank space
        # prints statement cancelling order
        print("Order cancelled")
        print("You can restart your order or exit the BOT")
        # proceeds to next function
        new_exit()


# defines function as new_exit
# allows user to make a new order or exit the BOT


def new_exit():
    # takes constants LOW and HIGH as parameters
    # also takes question as parameter
    # no returns
    print()  # prints blank space
    question = (f"Please enter a number between {LOW} and {HIGH} ")
    print("Would you like to make another order or exit?")
    print("To make another order, please enter 1")
    print("To exit the BOT, please enter 2")
    # asks user for input
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print()
        # prints selected option - new order
        print("New Order")
        print()
        # clears data from all lists
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # returns to main
        main()
    elif confirm == 2:
        print()
        # prints selected option - exit (bot)
        print("Exit")
        # clears data from all lists
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # exits program
        sys.exit


def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    # welcome function greets the user
    welcome()
    # order_type function asks the user whether their delivery is for
    # delivery or click and collect
    # calls either delivery_info or clickandcollect_info function
    del_pick = order_type()
    # order_cake functon allows user to choose how many cakes they are going to order
    # also allows user to choose their cake(s) from the menu
    order_cake()
    # print_order function prints order details
    # includes customer details, cakes ordered, and total cost details
    # if del_pick variable is for delivery, a $9 delivery charge may apply
    print_order(del_pick)
    # confirm_cancel function allows user to confirm or cancel order
    confirm_cancel()


# main function to run the entire program
main()
