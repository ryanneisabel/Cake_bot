# list of cake names
order_list = ['Vanilla Cake','Chocolate Cake','Strawberry Cake']
# list of cake prices
order_cost = [35, 35, 39.90]

cust_details = {'name':'Ryanne','phone':'1234567890', 'house': '13', 'street':'School', 'suburb':'Road'}


count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1


