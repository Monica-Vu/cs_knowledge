def top_k_most_frequent_elements(items, k):
    num_occurencs = generate_dict(items) 
    sorted_dict = sort_dict(num_occurencs)

    top_k_elements = list(sorted_dict.items())[-k:]
    top_k_list = []

    for item in top_k_elements:
        top_k_list.append(item[0])
    
    return top_k_list

def generate_dict(items): 
    num_occurences = {}

    for i in range(len(items)):
        if items[i] not in num_occurences.keys():
            num_occurences[items[i]] = 1
        else:
            num_occurences[items[i]] += 1
    
    return num_occurences

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def sort_dict(items):
    sorted_values = sorted(items.values())
    sorted_dict = {}

    for i in sorted_values:
        for key in items.keys():
            if items[key] == i: 
                sorted_dict[key] = items[key]
                break 
    
    return sorted_dict

sample = ['potato', 'potato', 'potato', 'tomato', 'tomato', 'farm']
print(top_k_most_frequent_elements(sample, 2))