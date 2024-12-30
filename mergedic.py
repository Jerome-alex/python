dict1_input = input("Enter the first dictionary (e.g., {'a': 1, 'b': 2}): ")
dict2_input = input("Enter the second dictionary (e.g., {'b': 3, 'c': 4}): ")

dict1 = eval(dict1_input)
dict2 = eval(dict2_input)

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)

