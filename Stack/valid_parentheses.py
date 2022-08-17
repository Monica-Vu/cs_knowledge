"""
* Intialize a dictionary with the closing brackets as the key 
* Iterate through the string
    * If it's a closing bracket and the length of the stack is 0, return false. Otherwise, check if the matching bracket exists.
    * If it's an opening bracket, add it to the stack
* Return true once you iterate through the entire array and stack is empty
"""

def valid_parentheses_01(string):      
    brackets = {"]": "[", "}": "{", ")": "("}
    stack = []

    for char in string:
        if char in brackets.values():
            stack.append(char)

        if char in brackets.keys(): 
            if len(stack) == 0:
                return False 
            
            if brackets[char] != stack.pop():
                return False
            
    return len(stack) == 0

print(valid_parentheses_01("()"))  # True 
print(valid_parentheses_01("{([])}"))  # True 
print(valid_parentheses_01("(]"))  # False 
print(valid_parentheses_01("]"))  # False 