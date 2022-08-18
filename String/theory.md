# Strings
* A sequence of immutable characters (you can also see a string as a string containing only characters)
* Each character has a index position, starting at 0

## Common Data Structures to Lookup Strings
* Trie
* Suffix Tree

## Common Algorithms to Lookup Strings
* Rabin Karp
* KMP

# Common Operations 
## Get length
```
s = "abced"

len(s)   # 5
```

## Get Index Position of a Character
Note that this built-in function only returns the index of first occurance of the character
```
s = "Hello world!"
s.index('o')    # 4 -> First 'o' is seen in position 4
```

## Count Number of Characters 
```
s = "Hello world!"
s.count('o')    # 2
```

## Reversing
```
s:[::-1]
```

## Convert All to Lowercase
```
s.lower()
```

## Convert All to Uppercase
```
s.upper()
```

## Check if String Starts With Something
```
s.startswith("Hell")  # True
s.startswith("hell")  # False
```

## Check if String Ends With Something
```
s.endswith("ld")    # True
s.endswith("LD")    # False
```

# Splitting 
`split()` takes an optional character of string. If you don't pass a parameter, it'll split based on whitespace of any size.
```
s.split()       # ['Hello', 'World!']
s.split(" ")    # ['Hello', 'World!']
s.split("  ")   # ['Hello World!']
```

## Splicing
Python has no substring methods (ex/ substring() or substr()). Instead, we use slice syntax to get parts of existing strings. The built-in function takes in three optional parameters: 
```
# Syntax: string[start: end: step]
s = "abcdef"

# Get all the characters until position 3 (exclusion)
s[:3] # 'abc'

# Get all the characters from position 3 until the end
s[3:] # 'def'

# Get all the characters from position 1 until the position 3 (exclusion)
s[1:3] # 'bc'

# Get every second character from index positions 1 to 5 (exclusion).
 s[1:5:2] # 'bd'

# Get every second character
 s[::2] # 'ace'
```

Note that you can also do negative indexing.

# Advantages
* There's often a string library in many programming languages, allowing strings to be dynamically allocated and often handles boundary issues.
* Often used as a base for many DTS (ex/  tries, suffix trees, suffix arrays, ternary search trees)

# Disadvantages
* Usually immutable
* Slow at performing operations (ex/ input, output)

# Common Terminology
**Anagram**: If you rearrange the letters of a word, it can produce a new or phrase.

**Palindrome**: a word, phase, number, or other sequence of characters that reads same forward or backwards. 

# Time Complexity
Assume that n represents the string's length.
| Operation        | Big O   | Notes |        
| ------------- |-------------| --------- |
| Access    | O(1) | |
| Search, Insert & Removal    | O(1) | You need to create a new string |

For the following table, assume that m represents the other string's length.

| Operation        | Big O   | Notes |        
| ------------- |-------------| --------- |
| Find substring    | O(nm) | This is the most naive case (i.e built-in cost) though typically costs O(n). You can read `Common Algorithms to Lookup Strings` to find more efficient algorithms|
| Concatenating   | O(n + m) | |
| Slice   | O(m) | |
| Split   | O(n + m) | |
| Strip   | O(n) | |

# Common Techniques
Many tips about Lists or Arrays are often applicable to strigs. 

## Counting Characters
Use a hash table, hash map, or a counter (could be built-in)

## Check if Two Strings Have An Intersection
Use a 26-bit bitmask to indicate which lower case latin character are inside the string. Two strings would have common characters if the intersection operation of the bits is non-zero.

```
mask = 0
for c in word:
  mask |= (1 << (ord(c) - ord('a')))
```

# Check if Two Strings are Anagrams

| Method        | Time Complexity  | Space Complexity | 
| ------------- |-------------| --------- |
| Sorting both strings   | O(n log (n))) | O(log(n)|
| Map each character to a prime number and multiple each mapped number together. Anagrams would have the same multiple (prime factor decomposition)   | O(n) | O(1)|
| Count the character frequency and check if they're the same | O(n) | O(1)|

# Check if a string is a palindrome
| Method        | Time Complexity  | Space Complexity | 
| ------------- |-------------| --------- |
| Reverse the string and check if it's equal to itself  | Cost of Reversing, which is O(n) | O(1) -> don't need to store anything technically|
| Two Pointers | O(n//2) | O(1) |

# Misc Technical Tips
Many tips about Lists or Arrays are often applicable to strigs. 

* Ask what are the possible characters and if it's case sensitive 

* The space complexity required for a counter is O(1), not O(n) as the upper bound is the total number of latin characters (i.e constant == O(1))

* **Corner Cases**: Empty String, String with 1-2 characters, String with repeated characters, Strings with only distinct characters 

# Sources 
https://www.techinterviewhandbook.org/algorithms/string/

https://stackoverflow.com/questions/35220418/runtime-of-pythons-if-substring-in-string

https://stackoverflow.com/questions/37606159/what-is-the-time-complexity-of-python-list-reverse

https://www.w3schools.com/python/python_ref_string.asp

https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-string/

https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/

https://www.learnpython.org/en/Basic_String_Operations