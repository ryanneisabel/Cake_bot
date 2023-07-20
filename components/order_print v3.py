# list of cake names
order_list = ['Vanilla Cake','Chocolate Cake','Strawberry Cake']
# list of cake prices
order_cost = [35, 35, 39.90]

cust_details = {'name':'Ryanne','phone':'1234567890', 'house': '13', 'street':'School', 'suburb':'Road'}

total_cost = sum(order_cost)

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"The total cost of the order is: ${total_cost:.2f}")

print_order()



