# Lists (Python)
* ordered sequence: each element in a list is identified by an index starting from 0
* can store different
* each item is seperated by a comma (,) 
* mutable: can be modified after creation. Each item is represents 
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
TODO: fill this section

# Common Techniques 
* Sliding Window 

# Misc Tips in Technical Interview Problems
* If the list is partially sorted or fully sorted, you can likely do binary search
* Assuming that order of elements do not have to be preserved, see if sorting the list can simplify the problem
* Be careful of going out of bounds! 
* **Check for corner cases:** empty, 1-2 elements, and repeated elements 

# Sources 
https://www.analyticsvidhya.com/blog/2021/04/python-list-programs-for-absolute-beginners/

https://techinterviewhandbook.org/algorithms/array/