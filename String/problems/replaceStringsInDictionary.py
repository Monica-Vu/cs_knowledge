def replace_string_val_in_dictionary(dictionary, string):
    if not dictionary:
        return dictionary

    string = string.lower()
    
    for key, value in dictionary.items():
        if isinstance(value, str) and string in value.lower(): 
            dictionary[key] = value.replace(string, "")
    
    return dictionary

print(replace_string_val_in_dictionary({"key1": "the zoo is great!", "key2": "I like going to the zoo", "key3": "zebras live in zoos."}, "zoo"))
print(replace_string_val_in_dictionary({}, "zoo"))
print(replace_string_val_in_dictionary({"key1": 1, "key2": "no zoo"}, "zoo"))
print(replace_string_val_in_dictionary({"key1": 1, "key2": "no"}, "zoo"))