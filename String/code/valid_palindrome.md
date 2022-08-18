# Question
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
* 1 <= s.length <= 2 * 105
* s consists only of printable ASCII characters.

# Questions
* Can I confirm what ASCII means? 
* It looks like we don't care if the strings are lower case or upper case?
* Do I have specific space or time constraints for now?

# Brainstorm
* One option is to remove non-alpahnumeric characters and lower case the string. 
* Then we would reverse the string.
* If they're equal, it's a palindrome.
* It would cost a lot due to having to remove punctuation, doing a lower case, and reversing the string. 

* We can use two pointers: one starting from index 0 and another starting in the last index
* While the right_pointer is greater than the left (or they haven't intersected yet), check if they're the same characters (not case sensitive so will need to use `lower` or `upper`). If they're not the same, we can return false. Otherwise, increase the pointer values.
* Since non-alphanumeric characters can occur and it's a palindrome if the alphanumeric characters are the same, we can move the pointer if we encounter a non-alphanumeric character. 
* It's a valid palindrome 

# Code
```
def isPalindrome(s: str) -> bool:
    left_pointer = 0
    right_pointer = len(s) - 1

    while left_pointer < right_pointer: 
        if not s[left_pointer].isalnum():
            left_pointer += 1
        
        elif not s[right_pointer].isalnum():
            right_pointer -= 1
        
        else: 
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False 

                left_pointer += 1
                right_pointer -= 1
        
    return True 

```

# Analysis (Two Pointers)
Time Complexity: O(n//2)
Space Complexity: O(1)

# Test Cases 
* Empty String
* String with only non-alphanumeric characters but under ASCII
* String with length 1 
* String with length 2 (palindrome)
* String with length 2 (not palindrome)
* Typical string size (palidrome)
* Non-typical string size (not palindrome) 
* Maximum Possible Length (palidrome)
* Maximum Possible Length (not palidrome)