# menu allowing user to choose between delivery or click and collect

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

    
    

