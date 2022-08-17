# Ask Questions & Clarify Requirements 
* Re-read the question and make notes or diagrams 
* Go through each provided example and ensure you understand what's happening 
* Be aware of any contraints **ex/ time, space, valid operations**

## Questions to Consider
* What is the input data am I provided? (type and format)
* What output data expecated? (type and format). Clarify if you need to return the exact data structure OR if the information itself is returned. 
* What are the minimum and maximum values for the input data?
* Is the input always valid? If not, what are the edge cases?
* Generate some test cases and the expected output if possible. Expand beyond the given examples. 
* Will I need to (or would it be helpful) to transform my data?
    * Sometimes, sorted elements in a list can be helpful 
    * If you need to consistently get a value, maybe changing it to a dictionary
* Are there any crucial information I need to know? 

# Before Starting The Question
* Ask the interviewer if they're familiar with the programming language syntax
    * If they're not, do your best to explain as you go

# Brainstorm
* Try to express your ideas in a concise, verbal manner
* State why you think something might work (or why it might not)
* State ideas even if you're unsure 
* Better to have a solution than no solution (don't strive for perfection)
* When appropriate, use technical terms ex/ memoization, names of algorithmic techniques, pass by reference/value

# Algorithm
* Once you decided with the interviewer(s) which method you will go for, try to write an algorithm or pseudocode
* Try to break parts into the smallest pieces possible to make it easier to create pure functions to break down your work and reduce work 
* Check the concatenation of values are of the same type if there's no automatic type coercion 
ex/ In JavaScript, if you do "1" + 1, it returns "11" 
* Avoid using global variable when possible 
* If you're cutting corners, state to the interviewer you are ex/ "In normal conditions, I would write a regex to parse this string rather not `split()`, which may not cover all cases."

# Write Your Code
* As you go through your code, mention what need you plan to implement 
* Explain why you might be writing particular syntax 
* Ideally the easiest part if you know your chosen language well enough

# Testing & Reflection 
* Write test cases (ensure you cover the typical and edge cases). While doing these tests, do a dry-run, comment the value of any variables declared or used

## Test Case to Consider
* Null Values 
* Empty Values
* Only 1 value of the subtype ex/ one character for strings, one item for bigger data structures
* Negative Values
* Zero
* Different type of input that one being expected 
* Off-by-one errors 

* State the time complexity and space complexity
* Talk about possible improvements (and implement if time permits)
Tip: To increase speed of a program, you can chose a better data structure or algorithm OR use more memory ex/ use a hash map/dictionary and a doubly linked list to get O(1) time complexity for `get` and `put` operation in LRU cache

# Sources