withdraw = eval(input("enter amount to withdraw: "))
if withdraw <= 2000.00:
    print('Hey', withdraw, "rs has been debited from your account")
    print("Remaing balance :" ,2000.00-withdraw, 'rs')
else:
    print("insufficent funds")