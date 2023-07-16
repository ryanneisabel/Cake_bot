import random
from random import randint

# list of random names
names = ["Nadia","Alissa","Courtney","Mia","Emma","Jasper","Loui","Harry","Joe","Zachary"]

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






def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    welcome()
    order_type()

main()



