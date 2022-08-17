# Problem 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

# Brainstorm
Input: A string containing only parentheses ('()[]{}')
Output: a boolean to indicate if the string is a valid parenthesis 

* We can use a stack to store the bracket we've seen so far 
* When we encounter an opening bracket, we add it to the stack
* When we encounter a closing bracket, we pop the last item (if it's not empty) from the stack and check if it's the right bracket
* If it's not, return false. Otherwise continue.

# Algorithm
* Intialize a dictionary with the closing brackets as the key 
* Intialize an empty list as  stack
* Iterate through the string
    * If it's an opening bracket, add it to the stack
    * If it's a closing bracket and If the stack's length is 0 or the brackets don't match, return False 
* Return true once you iterate through the entire array and stack returns empty
