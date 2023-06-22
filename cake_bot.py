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

def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    welcome()

main()



