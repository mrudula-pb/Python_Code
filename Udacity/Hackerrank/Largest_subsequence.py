# Input : "abcd", "abc"
# Output : 4
# The longest subsequence is 4 because "abcd"
# is a subsequence of first string, but not
# a subsequence of second string.
#
# Input : "abc", "abc"
# Output : 0
# Both strings are same, so there is no
# uncommon subsequence.

def largest_subsequence(str1, str2):
    length_str1 = len(str1)
    length_str2 = len(str2)

    if length_str1 == length_str2:
        return length_str1
    for i in range(length_str1):
        
    pass

str1 = "abcdef"
str2 = "defghi"
largest_subsequence(str1, str2)