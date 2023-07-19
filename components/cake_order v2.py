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
 
def menu():
    number_cakes = 12

    for count in range (number_cakes):
        print("{} {} ${:.2f}" .format(count+1,cake_names[count],cake_prices[count]))

menu()

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

print(num_cakes)

# choose cake from menu
print("Please choose your cake by entering the number from the menu ")
for item in range(num_cakes):
    while num_cakes > 0:
        cakes_ordered = int(input())
        order_list.append(cake_names[cakes_ordered])
        order_cost.append(cake_prices[cakes_ordered])
        num_cakes = num_cakes-1






