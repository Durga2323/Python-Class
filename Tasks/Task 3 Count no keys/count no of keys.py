# a = ['rajesh','ramesh','rajesh','venkatesh',100,50,'hyderabad',100,'hyderabad',45,'hyderabad']

# required output :- {'rajesh': 2, 'ramesh': 1, 'venkatesh': 1, 100: 2, 50: 1, 'hyderabad': 3, 45: 1}

a = ['rajesh','ramesh','rajesh','venkatesh',100,50,'hyderabad',100,'hyderabad',45,'hyderabad']

c = {ele:a.count(ele) for ele in a}
print(c)

# output :- {'rajesh': 2, 'ramesh': 1, 'venkatesh': 1, 100: 2, 50: 1, 'hyderabad': 3, 45: 1}