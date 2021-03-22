# A palindrome is a word that is the reverse of itself—that is,
# it is the same word when read forwards and backwards.
#
# For example:
#
# "madam" is a palindrome
# "abba" is a palindrome
# "cat" is not
# "a" is a trivial case of a palindrome

# NON-RECURSIVE SOLUTION METHOD
# class is_palidrome:
#     def is_palindrome(self, input):
#         reverse_input = input[::-1]
#         if input == reverse_input:
#             return True
#         return False
#
# solution = is_palidrome()
# input = "a"
# value = solution.is_palindrome(input)
# print(value)

# RECURSIVE SOLUTION METHOD
class is_palidrome:
    def is_palindrome(self, input):
        input_length = len(input)
        if input_length <= 1:
            return True
        else:
            if input[0] == input[input_length-1]:
                input_new = input[1:input_length-2]
                return self.is_palindrome(input_new)
            return False

solution = is_palidrome()
input = "MADAM"
value = solution.is_palindrome(input)
print(value)