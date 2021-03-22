import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        alphanumeric = ""
        for character in lower_case:
            if character.isalnum():
                alphanumeric += character
        total_str_len = len(alphanumeric)
        str_index_len = total_str_len - 1
        index = 0
        while index < (total_str_len/2) :
            if alphanumeric[index] == alphanumeric[str_index_len - index]:
                index += 1
            else:
                return False
        return True




obj = Solution()
value = obj.isPalindrome("A man, a plan, a canal: Panama")
print(value)