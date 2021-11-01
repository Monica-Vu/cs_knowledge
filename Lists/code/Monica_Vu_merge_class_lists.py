"""
2c.In the language of your choice, write a library function that solves this problem using one of your described approaches.
"""
# Library Function
def merge_class_lists(list_a, list_b):
    if len(list_a) == 0:
        return list_b 

    if len(list_b) == 0:
        return list_a

    unified_class_list = set() 

    for i in range(len(list_a)):
        unified_class_list.add(list_a[i])

    for j in range(len(list_b)):
        unified_class_list.add(list_b[j])

    return list(unified_class_list)

# Student class to make test cases 
class Student:
    def __init__(self, name):
        self.name = name

A = Student("Anna").name
B = Student("Bob").name
C = Student("Cindy").name
D = Student("Dan").name
E = Student("Ed").name
F = Student("Fay").name

list1 = [A, B, C]
list2 = [B, D, E, F]


# Test Cases
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("Test Case", "Input", "Expected Output", "Actual Output"))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("Empty Lists", "[], []", "[]", str(merge_class_lists([], []))))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("First list is empty", "['Anna', 'Bob', 'Cindy'], []", "['Anna', 'Bob', 'Cindy']", str(merge_class_lists([], list1))))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("Second list is empty", "[], ['Anna', 'Bob', 'Cindy']", "['Anna', 'Bob', 'Cindy']", str(merge_class_lists(list1, []))))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("One duplicate in both lists", "['Bob', 'Dan', 'Ed', 'Fay'], ['Anna', 'Bob', 'Cindy']", "['Ed', 'Dan', 'Cindy', 'Bob', 'Fay', 'Anna']", str(merge_class_lists(list1, list2))))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("One student in both lists", "['Bob'], ['Bob']", "['Bob']", str(merge_class_lists([B], [B]))))
print("{:<30} | {:<60} | {:<80} | {:<80} ".format("One student in both lists", "['Ed', 'Bob', 'Fay'] , ['Bob', 'Fay', 'Ed'] ", "['Bob']", str(merge_class_lists([E, B, F],[F, B, E]))))