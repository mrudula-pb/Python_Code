def has_common_ancestor(parent_child_pairs, node1, node2):
    dic = {}
    for pair in parent_child_pairs:
        if pair[1] not in dic:
            dic[pair[1]] = [pair[0]]
        else:
            dic.get(pair[1]).append(pair[0])

    def helper(dic, parents, node):
        if not node or node not in dic:
            return

        for x in dic.get(node):
            parents.append(x)
            helper(dic, parents, x)

    p1, p2 = [], []

    helper(dic, p1, node1)
    helper(dic, p2, node2)

    return len(p2) + len(p1) != len(set((p2 + p1)))

parent_child_pairs_2 = [(11, 10), (11, 12), (2, 3), (10, 2), (10, 5), (1, 3), (3, 4), (5, 6), (5, 7), (7, 8),]

parent_child_pairs_1 = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),(4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]


value = has_common_ancestor(parent_child_pairs_1, parent_child_pairs_2)
print(value)