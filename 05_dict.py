#  keys in dict are immutable datatypes --> cannot be changed
# if ovverriden latest value will be added

sample_dict = {1: 0, 2: 4, 3: 9}

print(sample_dict)
print(sample_dict[3])

sample_dict = {1: 2, 2:5, 3: 9, 3: 15}
print(sample_dict[3])

# combining tuple and dict variables-->
sample_dict = {(1, 2, 3, 4) : 1, 2: 4, 3: 9}
print(sample_dict)


dict_keys = sample_dict.keys()
dict_values = sample_dict.values()
dict_items = sample_dict.items()
print(dict_keys, dict_values, dict_items)


#  What happens if we access a key that is not present in dict --> we get none if we use get
sample_dict = {1: 2, 2:5, 3: 9, 3: 15}
print(sample_dict.get(6))

#  Adding elements to dict
sample_dict = {1: 2, 2:5, 3: 9, 3: 15}
sample_dict[4] = 16
print(sample_dict)


