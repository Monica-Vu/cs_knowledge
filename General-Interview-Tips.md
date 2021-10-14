# General Tips (for Techical Interviews)
* Clarify any assumptions made subconsciously **ex/ the types of parameters passed, if the parameters passed are always valid, the expected output (is the information OK or does it have to be exact format)**

**Inputs to Check For (If Input is Not Always Valid)**
* Invalid
* Empty
* Negative
* Different Type

* Be aware of any contraints **ex/ time, space, valid operations**

* Check for Off-by-one Errors

* Check the concatenation of values are of the same type if there's no automatic type coercion 

* ALWAYS test your code (at least do a dry-run and comment beside what the current input is)

* Write pure functions as much as possible to break down your work and reduce bugs 

* Avoid using global variables when possibles 

* To increase speed of a program, you can chose a better data structure or algorithm OR use more memory ex/ use a hash map/dictionary and a doubly linked list to get O(1) time complexity for `get` and `put` operation in LRU cache

* If you're cutting corners, state to the interviewer you are ex/ "In normal conditions, I would write a regex to parse this string rather not `split()`, which may not cover all cases."