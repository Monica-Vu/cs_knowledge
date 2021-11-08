# About
* A data structure where each item is a key-value pair. 
* All keys must be unique and is how we accessed each element.
* Values are accessed via key

# Methods
## Creation
* Use `{}` or `dict()`
```
dict_a = {}
dict_b = dict()
```
## Intialization
```
dict_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
dict_b = dict({'A': 'Apple', 'B': 'Ball', 'C': 'Cat'})
```

## Printing the Dictioary as Formatted
Get name of the dictionary and pass it to a built-in print function

```
print(dict_a)   # returns format of {key1: val1, key2: val2}
```

## Add an Element
```
# Create a key called 'A' that is paired with the value 'Apple'
dict_a['A'] = 'Apple'
```

```
dict_a.update({'D': 'Dog'})
```

## Get All Keys of Dictionary
```
dict_a.keys()   # returns dict_keys([key1, key2, key3])
```

## Get All Values of Dictionary
```
dict_a.items()   # returns dict_values([('key1', 'val1'), ('key2', 'val2')])
```

# Iterating
You need to iterate through the keys to access the dictionary

```
for key in dict_a.keys(): 
    . . .
```

```
for key in dict_a.: 
    . . .
```


# Accessing a Dictionary via Key
For the followin to work, you need to make sure the key exists.
```
dict_a['A']
```

This is a good option as it returns `None` or an object of your choice if it returns nothing
```
dict_a.get(Z)   # returns None 
dict_a.get(Z, "Key does not exist")   # returns "Key does not exist" 
```

## Accessing a Dictionary via Index
Convert dictionary to lists (no guranteed on order)
```
dict_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
list(dict_a.keys())[0]

list(dict_a.keys())[-1]

list(dict_a.values())[0]

list(dict_a.values())[-1]
```

## Deleting a Key
```
del dict_a[key]
```

```
dict_a.pop(key)
```

## Deleting Keys
* Use any function mentioned in `Deleting a Key` 

## Merging Dictinaries 
Python 3.5: Use the unpacking operator (**) to create a dictionary from the two smaller dictionaries. You can add as many dictionaries between the braces.

```
dic_a = {'A': 'Apple', 'B': 'Ball'}
dic_b = {'C': 'Cat', 'D': 'Dog'}
dic_merged = {**dic_a, **dic_b}
print (dic_merged)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
```

If you don't want to create a new dictionary, you can use `update`. Note if there are two duplicate keys, it will take the value of the one being concantenated. 
```
dic_a = {'A': 'Apple', 'B': 'Ball'}
dic_b = {'C': 'Cat', 'D': 'Dog'}
dic_a.update(dic_b)
print (dic_a)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
```

Python 3.9+: Use the `|` operator to concatenate >= 2 dictionaries 
```
dic_a = {'A': 'Apple', 'B': 'Ball'}
dic_b = {'C': 'Cat', 'D': 'Dog'}
dic_c = dic_a | dic_b
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}

# Concatenating more than 2 dictionaries
dic_d = dic_a | dic_b | dic_c
```

## Updating key-value pairs 
```
dic_a['A'] = 'Apricot'
```

## Sorting Using Keys
If your keys are string, they can be sorted alphabetically when in the form of a list.
```
dic_a = {'B': 100, 'C': 10, 'D': 90, 'A': 40}
sorted(dic_a.items(), key=lambda x: x[0])
>>> [('A', 40), ('B', 100), ('C', 10), ('D', 90)]

dic_a = {'B': 100, 'C': 10, 'D': 90, 'A': 40}
sorted(dic_a.items(), key=lambda x: x[0], reverse=True)
>>> [('A', 40), ('B', 100), ('C', 10), ('D', 90)]
```

## Create Dictionary Dynamically
If keys are values:
```
dict_c = {i: i**2 for i in range(5)}
print(dict_c)
>>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

If keys are strings, you need to use "f-stirngs":
```
dict_c = {f'{i}: i**2 for i in range(5)}
print(dict_c)
>>> {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16}
```

## Create a dictionary from lists 
```
names = ['Sam', 'Adam', 'Tom', 'Harry']
marks = [90, 85, 55, 70]

dict_grades = dict(zip(names, marks))
print (dic_grades)
>>> {'Sam': 90, 'Adam': 85, 'Tom': 55, 'Harry': 70}
```

## Referencing a Dictionary
When you referece a dictionary, it means that any changes applied to the dicitonary that is getting referenced 

```
dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
dic_b = dic_a       # Simple reassignment (Reference assignment)

dic_b['D'] = 'Dog'
print (dic_b)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
print (dic_a)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
```

## Shallow Copy
Use `copy()` function if you want to get just gt the intial values. 
```
dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
dic_b = dic_a.copy()

dic_b['D'] = 'Dog'

# New, shallow copy, has the new key-value pair
print (dic_b)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}

# The parent dictionary does not have the new key-value pair
print (dic_a)
>>> {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
```

However, if you modify the dictionary with mutable objects that is getting referenced, these changes will also be seen with the previous dictionary. 
```
dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
dic_b = dic_a.copy()

dict_b['A]
```

## Renaming Existing Keys
* Pop the value with the key you want to rename
* Insert the new key into the dictionary with the value from above
```
dict_a = {'Sam': 90, 'Adam': 85, 'Tom': 55, 'Harry': 70}

dict_a['Alex'] = dic_a.pop('Adam')

print (dict_a)
>>> {'Sam': 90, 'Tom': 55, 'Harry': 70, 'Alex': 85}
```

## Check if Key Exists
```
dic_a = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
'A' in dic_a
# True

'E' in dic_a
# False
```