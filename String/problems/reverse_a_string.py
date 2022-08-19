def reverse_using_for_loop(s: str):
    reversed_string = ""

    for char in s:
        reversed_string = char + reversed_string
    
    return reversed_string

def reverse_using_while_loop(s: str): 
    reversed_string = ""

    count = len(s)

    while count > 0:
        reversed_string += s[count - 1]
        count -= 1
        
    return reversed_string

s = "Hello World"
print(reverse_using_for_loop(s))
print(reverse_using_while_loop(s))

# Source: https://www.scaler.com/topics/how-to-reverse-a-string-in-python/