def check_phone(question,PH_LOW,PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0 
            while test_num > 0: 
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number ")

question = ("Please enter your phone number ")
PH_LOW = 7
PH_HIGH = 10



phone = check_phone(question,PH_LOW,PH_HIGH)
print(phone)


