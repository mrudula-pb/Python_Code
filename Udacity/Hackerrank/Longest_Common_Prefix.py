# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"

def lc_prefix(str_value):
    prefix = []
    length_str = len(str_value)
    for x in zip(*str_value):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break
    return "".join(prefix)

str_value = ["flower", "flow", "flight"]
value = lc_prefix(str_value)
print(value)