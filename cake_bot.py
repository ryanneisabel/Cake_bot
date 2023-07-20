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
# list to store order list
order_list = []
# list to store order cost 
order_cost = []

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
    del_pick = ""
    print("Do you want your cake to be delivered, or will you be picking it up?")
    print("For delivery, enter 1")
    print("For click and collect, enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Delivery")
                    del_pick = "delivery"
                    delivery_info()
                    break
                elif delivery == 2:
                    print("Click and Collect")
                    del_pick = "click and collect"
                    clickandcollect_info()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("This is not a valid input")
            print("Please enter 1 or 2 ")
    return del_pick

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

def menu():
    number_cakes = 12
    for count in range (number_cakes):
        print("{} {} ${:.2f}" .format(count+1,cake_names[count],cake_prices[count]))

def order_cake():
# ask for total number of cakes for order
    num_cakes = 0
    while True: 
        try: 
            num_cakes = int(input("How many cakes do you want to order? "))
            if num_cakes >= 1 and num_cakes <= 12:
                break
            else:
                print("Your order must be between 1 and 12 ")
        except ValueError:
            print("This is not a valid number ")
            print("Please enter a number between 1 and 12")
    # choose cake from menu
    for item in range(num_cakes):
        while num_cakes > 0:
            while True:
                try:
                    cakes_ordered = int(input("Please choose your cake by entering the number from the menu "))
                    if cakes_ordered >= 1 and cakes_ordered <= 12:
                        break
                    else:
                        print("Your cake must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")
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
        print()
        print("Your order is for Delivery. A $9 delivery charge will apply.")
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
    print("Total Order Cost")
    print(f"The total cost of the order is: ${total_cost:.2f}")






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
    


main()



