
# Given two strings s and t , write a function to determine if t is an anagram of s.

def isAnagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    length_s = len(sorted_s)
    length_t = len(sorted_t)
    if length_s == length_t:
        for x,y in zip(sorted_s, sorted_t):
            if x != y:
                return False
            else:
                continue
        return True
    return False
s = "a"
t = "ab"
value = isAnagram(s, t)
print(value)