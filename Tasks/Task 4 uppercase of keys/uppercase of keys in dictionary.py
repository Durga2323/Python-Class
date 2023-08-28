# dict1={
#     "asaa":"asaa",
#     "fsaf":"fsaf",
#     "gagd":{
#         "data":"data",
#         "value":"value",
#         "info":{
#             "compress":"compress",
#             "product":"product",
#             "data1":{
#                 "goon":"goon"
#             }
#         }
#     },
#     "sample":"sample"
# }

# -----------------------------------------

# def convert_keys_to_uppercase(dictionary):
#     new_dict = { }
#     for key,value in dictionary.items():
#         if isinstance(value,dict):
#             new_dict[key.upper()]=convert_keys_to_uppercase(value)
#         else:
#             new_dict[key.upper()]=value
#     return new_dict

# dict_upper_keys=convert_keys_to_uppercase(dict1)

# print(dict_upper_keys)

# ------------------------------------
# key1 = dict1.keys()
# dict2=dict1['gagd']
# key2=dict2.keys()
# dict3=dict2['info']
# key3=dict3.keys()
# dict4=dict3['data1']
# key4=dict4.keys()
# def up_keys(a,b,c,d):
#     return key1,key2,key3,key4
# # def up_keys2(b):
# #     return dict2
# # print(dict1)
# # print(dict2)
# # print(dict3)
# # print(dict4)

# all_keys = [up_keys(key1,key2,key3,key4)]
# dict1.update(all_keys)
# print(all_keys)

# print(dict1)

# print(dict2)

# ------------------------------------


# def up_keys(a):
#     if dict1.keys() in dict1:
#         return ele.upper()
#     else:
#         return a[-1]

# print(up_keys(dict1))


#--------------------------------------------------------------------
dict1={
    "asaa":"asaa",
    "fsaf":"fsaf",
    "gagd":{
        "data":"data",
        "value":"value",
        "info":{
            "compress":"compress",
            "product":"product",
            "data1":{
                "goon":"goon"
            }
        }
    },
    "sample":"sample"
}


def sample_dict(dict1):
    dict2={}
    for ele in dict1:
        if type(dict1[ele]) == dict:
            dict2[ele.upper()]=sample_dict(dict1[ele])
        else:
            dict2[ele.upper()] = dict1[ele]
    return dict2

print(sample_dict(dict1))




