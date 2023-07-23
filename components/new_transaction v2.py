import sys

# list to store ordered cakes
order_list = []
# list to store cost of cakes
order_cost = []

# customer details dictionary
customer_details = {}

def main():
    print("Start again")

print("Would you like to make another order or exit?")
print("To make another order, please enter 1")
print("To exit the BOT, please enter 2")
while True:
    try:
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("New Order")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                main()  
                break

            elif confirm == 2:
                print("Exit")
                sys.exit
                break
        else: 
            print("The number must be 1 or 2 ")
    except ValueError: 
        print("This is not a valid number")
        print("Please enter 1 or 2")
            
     