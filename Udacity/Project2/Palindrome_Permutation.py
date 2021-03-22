
# Given a string, determine if a permutation of the string could form a palindrome.
# Input: s = "aab"
# Output: True
# Explanation:
# "aab" --> "aba"
#
#
# Input: s = "code"
# Output: False
# Explanation:
# No solution

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    def __setitem__(self, key, value):


dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)

# s = "aab"
# palin_perm(s)