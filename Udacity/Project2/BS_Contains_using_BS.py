def recursive_binary_search(target, source):
    if len(source) == 0:
        return False
    center = (len(source) - 1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:])
    else:
        return recursive_binary_search(target, source[:center])


def contains(target, source):
    return recursive_binary_search(target, source)


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))  ## True
print(contains('c', letters))  ## True
print(contains('b', letters)) ## False