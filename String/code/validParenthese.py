"""
Given a string with parenthese, validate if this is balanced. A balanced string 

QUESTIONS:
1. What is the input? Are there words or just parentheses? 
2. Should I consider future issues (ex/ different types of brackets or specific cases -- i.e :) might mean happy
3. What's the maximum and minimum input size? 

"""
def valid_parentheses(string):
    numOpeningBrackets = 0

    for char in string:  
        if char == ")" and numOpeningBrackets == 0: 
            return False 
        if char == "(": 
            numOpeningBrackets += 1 
        if char == ")":
            numOpeningBrackets -= 1

    if numOpeningBrackets == 0:
        return True 
    else: 
        return False 
        
# print(valid_parentheses(""))    # expect: True
# print(valid_parentheses("()"))    # expect: True
# print(valid_parentheses("("))    # expect: False
# print(valid_parentheses(")"))    # expect: False
# print(valid_parentheses("())"))    # expect: False
# print(valid_parentheses("((()))"))    # expect: True
# print(valid_parentheses("((())))"))    # expect: False
# print(valid_parentheses("() ()"))    # expect: True
# print(valid_parentheses("() () ("))    # expect: False

def valid_different_parentheses(string): 
    brackets = {"[": "]", "{": "}", "(": ")"}
    stack = []

    for char in string: 
        if char in brackets.values():
            if len(stack) == 0:
                return False 

            popped = stack.pop()

            if char == brackets[popped]:
                continue 
            else:
                return False

        if char in brackets.keys(): 
            stack.append(char) 

    if len(stack) == 0:
        return True
    else:
        return False 

print(valid_different_parentheses(""))    # expect: True

print(valid_different_parentheses("()"))    # expect: True
print(valid_different_parentheses("[]"))    # expect: True
print(valid_different_parentheses("{}"))    # expect: True

print(valid_different_parentheses("("))    # expect: False
print(valid_different_parentheses(")"))    # expect: False
print(valid_different_parentheses("["))    # expect: False
print(valid_different_parentheses("]"))    # expect: False
print(valid_different_parentheses("{"))    # expect: False
print(valid_different_parentheses("}"))    # expect: False

print()
print(valid_parentheses("())"))    # expect: False
print(valid_parentheses("{[()]}"))    # expect: True
print(valid_parentheses("((())))"))    # expect: False
print(valid_parentheses("() []"))    # expect: False
print(valid_parentheses("() [}"))    # expect: False
print(valid_parentheses("() {} ["))    # expect: False