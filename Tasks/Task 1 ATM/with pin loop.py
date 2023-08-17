for attempt in range(3):
    pin = int(input("Enter your pin: "))
    if pin == 1234:
        account_type1 = input("enter your account type: ")
        if account_type1 == "savings":
            withdraw = eval(input("enter amount to withdraw: "))
            if withdraw <= 2000.00:
                print('Hey', withdraw, "rs has been debited from your account")
                print("Remaing balance :" ,2000.00-withdraw, 'rs')
            else:
                print("insufficent funds, Please try again.")
                break
        else:
            print("Invalid account type, Please try again later.")
            break
    else:
        print("invalind pin, Please try again.")


if attempt == 2:
    print("You have entered 3 wrong pin's, please try again after 24 hours.")
