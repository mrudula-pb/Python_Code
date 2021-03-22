
output = [[]]

def groupAnagrams(strs):
    d = {}
    for i in range(len(strs)):
        x = ''.join(sorted(strs[i]))
        if x not in d:
            d[x] = [strs[i]]
        else:
            d[x].append((strs[i]))
    return d.values()
    # length = len(strs)
    # for i in range(length):
    #     for j in range(i+1,length):
    #         if len(strs[i]) == len(strs[j]) and sorted(strs[i]) == sorted(strs[j]):
    #             if strs[i] not in output:
    #                 output.append(strs[i])
    #             if strs[j] not in output:
    #                 output.append(strs[j])
    #             continue
    #
    # return output


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

value = groupAnagrams(strs)
print(value)