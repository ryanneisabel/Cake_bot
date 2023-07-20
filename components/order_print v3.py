# list of cake names
order_list = ['Vanilla Cake','Chocolate Cake','Strawberry Cake']
# list of cake prices
order_cost = [35, 35, 39.90]

cust_details = {'name':'Ryanne','phone':'1234567890', 'house': '13', 'street':'School', 'suburb':'Road'}

# print customer details
print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}" 
      .format(cust_details['name'],"\n",cust_details['phone'],"\n",cust_details['house'],"\n",cust_details['street'],"\n",cust_details['suburb']))

count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1



