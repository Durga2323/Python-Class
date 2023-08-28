# name = input("enter your string")

# o = eval(input("which occurance of a :"))

# A1= name.index("a")

# A2= name.index("a", A1 + 1)

# A3= name.index("a", A2 + 1)

# A4= name.index("a", A3 + 1)

# if o == 1:
#     print(A1)
# elif o == 2:
#     print(A2)
# elif o == 3:
#     print(A3)
# elif o == 4: # checking after reinstall
#     print(A4)
# else:
#     print("a is occured only",name.count("a"),"times, try with the value <=", name.count("a"),".")


# 2 method:-

# string = input("Enter your string: ")
# alpha = input("enter the alphabet that you need to find: ")
# occurance = int(input(f"Which occurrence of {alpha} do you want to find? "))

# occurrences = string.count(alpha)

# print(f"No of {alpha}'s found in the entered string: ", occurrences)
# if occurance <= occurrences:
#     start_index = -1
#     for _ in range(occurance):
#         start_index = string.find(alpha, start_index + 1)
#     print(start_index)
# else:
#     print(alpha, f"occurs only {occurrences} times. Please try with a value <= {occurrences}.")

# 3rd method :-

string = input("Enter your string: ")

character = input("enter the character to findout: ")

z = string.find(character)

if z != -1:
    occurance = int(input(f"Which occurrence of {character} do you want to find? "))

    occurrences = string.count(character)

    print(f"No of {character}'s found in the entered string: ", occurrences)
    if occurance <= occurrences:
        start_index = -1
        for _ in range(occurance):
            start_index = string.find(character, start_index + 1)
        print(start_index)
    else:
        print(character, f"occurs only {occurrences} times. Please try with a value <= {occurrences}.")
else:
    print(character, "is not exits in the entered string.")