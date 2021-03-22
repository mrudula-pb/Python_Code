# Given a list of strings, group the strings that are equivalent when rotated.
# For example, the input
# ["abc", "bca", "cab", "xyz", "yzx", "cba", "aaaa"]
# should return the groups:
# {["abc", "bca", "cab"], ["xyz, "yzx"], ["cba"], ["aaaa"]}
#
# The order of the strings or the groups for the result does not matter.
# {["cba"], ["xyz, "yzx"], ["bca", "abc", "cab"], ["aaaa"]}
# is an acceptable solution too.

def groupRotatedStrs(str_list):
    dict = {}
    for word in str_list:
        sortedWord = "".join(sorted(word))
        if sortedWord not in dict:
            dict[sortedWord] = [word]
        else:
            dict[sortedWord].append(word)

    return list(dict.values())

str_list = ["abc", "bca", "cab", "xyz", "yzx", "cba", "aaaa"]
rotated_strs = groupRotatedStrs(str_list)
print(rotated_strs)