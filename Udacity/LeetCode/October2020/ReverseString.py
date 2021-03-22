
def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    print(our_string)
    str_indices = len(our_string) - 1
    print(str_indices)
    i = 0
    for element in range(str_indices):
        new_string = []
        new_string.append(our_string[str_indices - element]
        return new_string


reverse_str = string_reverser("water")
print(reverse_str)