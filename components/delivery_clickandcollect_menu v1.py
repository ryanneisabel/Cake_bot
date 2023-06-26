# bugs
# will only work for valid inputs, "d" and "c"
# invalid input triggers else statement but program does not ask for input again

# menu allowing user to choose between delivery or click and collect

print("Do you want your cake to be delivered, or will you be picking it up?")
print("For delivery, enter d")
print("For click and collect, enter c")

delivery = input()

if delivery == "d":
    print("Delivery")

elif delivery == "c":
    print("Click and Collect")

else:
    print("That input was invalid")

