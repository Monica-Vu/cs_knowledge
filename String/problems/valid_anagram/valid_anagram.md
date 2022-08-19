# Problem
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

# Questions
* Is an empty string considered anagram? I would say "yes."
* Any restrictions on how I tackle this problem (ex/ not allowed to used certain DTS)

# Brainstorm
* One option is to create a dictionary for each string and count the numbers of characters. If they contain the same number of characters, then the

* Another option is to sort the string using Python's built-in `sorted` function because sorting will put all the same letters together. If they're anagrams, then they should be exact the same. 

# Code (Sorted)
```
def is_anagram_sorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

## Analysis
Time Complexity: O(n log n) -> cost of sorted() twice but we ignore constants
Space Complexity: O(1) 

# Code (Using Dictionary)
```
def is_anagram_dict(s: str, t: str) -> bool:
    s_dict, t_dict = {}, {}

    # Note that get(char, 0) gets the current value of the key (char). If it doesn't exist, we automatically assign a value of 0.
    for char in s: 
        s_dict[char] = s_dict.get(char, 0) + 1
        
    for char in t: 
        t_dict[char] = t_dict.get(char, 0) + 1
    
    return s_dict == t_dict
```

## Analysis 
Time Complexity: O(n) -> need to iterate through both strings
Space Complexity: O(1) -> Since we're only dealing with lowercase strings, the worst case is that the dictionary has 26 letters with integers. 

# Test Cases 
* `s` and `t` are empty
* `s` contains lowercase letters and `t` is empty
* `t` contains lowercase letters and `s` is empty
* `s` and `t` are anagrams (normal case)
* `s` and `t` are not anagrams (normal case)
* `s` and `t` are anagrams (long case)
* `s` and `t` are not anagrams (long case)

# Resources 
https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).