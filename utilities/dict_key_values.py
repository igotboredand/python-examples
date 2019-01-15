def keys_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(k)
    return lst

def values_only(dict):
    lst = []
    for k, v in dict.items():
        lst.append(v)
    return lst

ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
}

keys_only_value = keys_only(ages) # ['Peter', 'Isabel', 'Anna']
values_only_value = values_only(ages) # [10,11,9]

print("Key values from dict: ", keys_only_value)
print("Values only from dict: ", values_only_value)



