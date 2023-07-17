# cake menu

cake_names = ['Vanilla Cake','Chocolate Cake','Strawberry Cake','Caramel Cake',
              'Red Velvet Cake','Carrot Cake','Lemon Cake' ,'Ice Cream Cake',
              'Vanilla Mousse Cake','Chocolate Mousse Cake','Black Forest Cake','Blueberry Cake']

cake_prices = [35, 35, 39.90, 39.90, 39.90, 39.90,
               39.90, 39.90, 39.90, 45, 49.90, 49.90]

number_cakes = 12

# print("How many pizzas would you like to order? ")
# num_cakes = int(input())

for count in range (number_cakes):
    print("{} {} ${:.2f}" .format(count+1,cake_names[count],cake_prices[count]))

