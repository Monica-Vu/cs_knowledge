def is_anagram_sorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def is_anagram_dict(s: str, t: str) -> bool:
    s_dict, t_dict = {}, {}

    # Note that get(char, 0) gets the current value of the key (char). If it doesn't exist, we automatically assign a value of 0.
    for char in s: 
        s_dict[char] = s_dict.get(char, 0) + 1
        
    for char in t: 
        t_dict[char] = t_dict.get(char, 0) + 1
    
    return s_dict == t_dict

print(is_anagram_sorted("silent", "listen"))
print(is_anagram_sorted("play", "playy"))
print(is_anagram_dict("silent", "listen"))
print(is_anagram_dict("play", "playy"))