def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    strip_str1 = str1.replace(" ", "").lower()
    strip_str2 = str2.replace(" ", "").lower()

    if len(strip_str1) == len(strip_str2):
        print(sorted(strip_str1))
        print(sorted(strip_str2))
        if sorted(strip_str1) == sorted(strip_str2):
            return True
    return False

v1 = anagram_checker('water', 'waiter')
print(v1)
v2 = anagram_checker('Dormitory', 'Dirty room')
print(v2)
v3 = anagram_checker('Slot machines', 'Cash lost in me')
print(v3)
v4 = anagram_checker('A gentleman', 'Elegant men')
print(v4)
v5 = anagram_checker('Time and tide wait for no man', 'Notified madman into water')
print(v5)
