# Lists 
* ordered sequence: each element in a list is identified by an index starting from 0
* In some languages, they're immutable (ex/ Java, C++) while in others, they're dynamic or can change in size (ex/ Python, JavaScript, Ruby, PHP)
* can store different data types (ame in Python)
* each item is seperated by a comma (,) 
* mutable: can be modified after creation. 
* you can use positive indexing (index starts from 0) or negative indexing (index starting from the end of the list)

## Example - List Creation
```
a = []
a = list()
a = ['Hello', 10, True, 2.0]
a = list('Hello', 10, True, 2.0()
```

## Example - Indexing
```
a = ['Hello', 10, True, 2.0]

a[1]    # equals to 10
a[-1]   # equals to 2.0
```

# Common Operations
## Sorting
use keywords `sort` or `sorted` 

The following changes the list diretly and doesn't return any value
```
list.sort(key =. . . , reverse)
```

The following doesn't change the list and returns the sorted list
```
list.sorted(key =. . . , reverse)
```

In both cases, there are two optional parameters:
**reverse**: Boolean represents if list is to be sorting is ascending or descending.
**key**: a f(x) used for sorting comparison. This would be useful in tuples or ditionaries. 

```
# We can sort based on length of item
sorted(list, key=len)

# sort based on the second element of the tuple 
def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

random.sort(key=takeSecond)
```

### Example Using Dictionary
```
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_name(employee):
    return employee.get('Name')

def get_age(employee): 
    return employee.get('age)

def get_salary(employee):
    return employee get('salary')

employees.sort(key=get_name)
employees.sort(key=get_age)
employees.sort(key=get_salary, reverse=True)
```

Alternatively, we could have use lambda functions if the function can be summarized as one line.

```
employees.sort(key=lambda x: x.get('Name))
employees.sort(key=lambda x: x.get('age))
employees.sort(key=lambda x: x.get('salary), reverse=True)
```

## Merging Two Lists (Built-in)
Use keyword `extend`

The following would create a new list with all the items from listA first and then the items from ListB. If you want the items from ListB to be first, you would switch the positions of ListA and ListB. 
```
listA.extend(listB)
```

## Switching Variable Names at the same time
Declare the variables in the same line with new values. 
```
listA = [1, 2, 3, 4, 5]
listA[0], listB[-1] = listB[-1], listA[0]

# Expected Output: [5, 2, 3, 4, 1]
```

## Checking if item exists in list
Use keyword `in` 
```
a = [1, 2, 3]

if 1 in a:
    print("1 exists in a")

# Expected Output: "1 exists in a"
```

Cost: O(n)

## Counting Number of Items
Use keyword `count` 
```
a = [1, 6, 1, 2, 7, 3, 7, 5, 6, 4, 5, 7]

a.count(1) # Expected Output: 2 (no return)
a.count(7) # Expected Output: 3 (no return)
```

Cost: O(n)

# Advantages
* Can store multiple items with one variable name (items are contigious in memory)
* Fast access to elements if you have an index

# Disadvantages 
* Addition and removal of elements except in the last positions are slow because the elements need to be shifted to accomdate the new or missing element 
* You may not be able to alter the size after intialization. In this case, you would need to make a new list and copy over the existing elements, which would take O(n) time.

# Common Terminology
**Subarray**: A range of contigious values within an array
Example: given an array [2, 3, 6, 1, 5, 4], [3, 6, 1] is a subarray while [3, 1, 5] is not a subarray.

**Subsequence:** A sequence that can be created by deleting some or no elements of a list without changing the order 
Example: given an array [2, 3, 6, 1, 5, 4], [3, 1, 5] is a subsequence but [3, 5, 1] is not a subsequence.

# Time Complexity
| Operation        | Big O   | Notes |        
| ------------- |-------------| --------- |
| Access    | O(1) | You know the index |
| Search      | O(n) |  |  
| Search (sorted array) | O(log (n))| Use binary search
| Insert or Remove at the end | O(1) | No elements need to be shifted|
| Insert or Remove everywhere else but the end| O(n) | You need to shift all elements by the left (removal) or the right (addition), which can cost up to O(n) |

# Common Techniques 
* Sliding Window: can be be applied with subarray or substring problems. It often uses **two pointers** as well. This ensures that each value is visited at most twice and time complexity is O(n) 

* Two Pointers: If given two lists or arrays to process, you can have one index per list/array to traverse and compare them and increment (or decrement) when relevant.

* You can see if traversing from the right versus the left might make it easier. 

* See if sorting the list or array can simplify the problem

* Using hashing, a prefix/suffix sum/product might be use [TODO: try to understand this more and solve problems relating]

* If given a sequence and O(1) is asked, you can possibly use a hashtable with the index as a hash. Example: if array only has values from 1 to N (length of array), negate the value at that index by one to indicate presence of the number. [TODO: try to solve a problem relating to this]

* Traversing the array more than once (as long as it's fewer than n times) is still O(n)

# Misc Tips in Technical Interview Problems
* If the list is partially sorted or fully sorted, you can likely do binary search
* Assuming that order of elements do not have to be preserved, see if sorting the list can simplify the problem
* Be careful of going out of bounds! 
* **Check for corner cases:** empty, 1-2 elements, duplicated elements 

# Sources 
https://www.analyticsvidhya.com/blog/2021/04/python-list-programs-for-absolute-beginners/

https://techinterviewhandbook.org/algorithms/array/

https://www.programiz.com/python-programming/methods/list/sort