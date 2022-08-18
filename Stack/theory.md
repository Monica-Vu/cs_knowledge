# Stack
* Abstract data type that allows you to perform operations on top of it (follows LIFO -- last in, first out)
* Can be implemented using a built-in classes (ex/ C++, Java) linked list, deque, queue, or a list (Python, Array)
    * The biggest issue with using a list DTS (at least in Python) is that there can be performance issues as the stack grows. Since the items in the list are stored next to each other in memory, Python would need to do some memory reallocation as it grows. Thus, some `append` calls can take longer

## Uses
* Supports nested or recursive f(x) calls
* Depth-first search 

## Example (Using Python)

# Operations
Note that we're using a list data structure.

## Inserting a New Item (Push)
```
s.append(item)
```

## Removing The Top Element (Pop)
Make sure to check if stack is empty!
```
s.pop() 
```

## Get the Top of the Element (Peek)
```
s[-1]
```

## Check if Stack is Empty 
```
if len(s) == 0
```

## Get Size
```
len(s)
```

# Common Terminology

# Advantages
* Regardless of the stack size, operations are typically O(1)
* Implementation is relatively straightforward

# Disadvantages
* No random access
* Can only perform performation at the top

# Time Complexity
| Operation        | Big O   |        
| ------------- |-------------| 
| Peek    | O(1) | 
| Push    | O(1) | 
| Pop    | O(1) | 
| isEmpty    | O(1) | 
| Search    | O(n) | 

# Common Techniques

# Misc Technical Tips
* **Corner Cases**: Empty, Stack with one or two item(s)

# Use Cases
* Undo/Redo 
* Going back and forth between browsers 

# Sources 
https://www.techinterviewhandbook.org/algorithms/stack/

https://www.geeksforgeeks.org/stack-in-python/

https://medium.com/basecs/stacks-and-overflows-dbcf7854dc67