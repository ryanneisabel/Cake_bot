question = "Enter your name "

while True:
    response = input(question)
    x = response.isalpha()
    if x == False:
        print("Input must only contain letters")
    else: 
        print(response.title())
        break

    