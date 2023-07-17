import random
from random import randint

# list of random names
names = ["Nadia","Alissa","Courtney","Mia","Emma","Jasper","Loui","Harry","Joe","Zachary"]
# list of cake names
cake_names = ['Vanilla Cake','Chocolate Cake','Strawberry Cake','Caramel Cake',
              'Red Velvet Cake','Carrot Cake','Lemon Cake' ,'Ice Cream Cake',
              'Vanilla Mousse Cake','Chocolate Mousse Cake','Black Forest Cake','Blueberry Cake']
# list of cake prices
cake_prices = [35, 35, 39.90, 39.90, 39.90, 39.90,
               39.90, 39.90, 39.90, 45, 49.90, 49.90]

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
                    delivery_info()
                    break

                elif delivery == 2:
                    print("Click and Collect")
                    clickandcollect_info()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("This is not a valid input")
            print("Please enter 1 or 2 ")

# delivery information - name, address, and phone number
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print(customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question )
    print(customer_details['house'])


    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question )
    print(customer_details['street'])


    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question )
    print(customer_details['suburb'])
    print(customer_details)
      

# click and collect information - name and phone number
def clickandcollect_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print(customer_details['phone'])
    print(customer_details)

# cake menu
def menu():
    number_cakes = 12
    for count in range (number_cakes):
        print("{} {} ${:.2f}" .format(count+1,cake_names[count],cake_prices[count]))












def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''

    welcome()
    order_type()
    menu()
    


main()



