import random
from random import randint

# list of random names
names = ["Nadia","Alissa","Courtney","Mia","Emma","Jasper","Loui","Harry","Joe","Zachary"]

# customer details dictionary
customer_details = {}

# validates input to check if left blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank ")

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
    print("Do you want your cake to be delivered, or will you be picking it up?")

    print("For delivery, enter 1")
    print("For click and collect, enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Delivery")
                    break

                elif delivery == 2:
                    print("Click and Collect")
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("This is not a valid input")
            print("Please enter 1 or 2 ")

# click and collect information - name and phone number
def clickandcollect_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print(customer_details['phone'])







def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    welcome()
    order_type()
    clickandcollect_info()

main()



