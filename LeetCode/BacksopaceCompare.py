import filecmp
import itertools
import operator


def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    f = open('/home/mdot/PycharmProjects/LeetCode/MyFile1.txt', 'w+')

    f.write(S)

    f = open('/home/mdot/PycharmProjects/LeetCode/MyFile2.txt', 'w+')

    f.write(T)

    return filecmp.cmp('MyFile1.txt', 'MyFile2.txt')


def backspace_process(a, b):
    print(str(a), ',', str(b))

    if a == '#':
        return b
    else:
        return a, b

def main():
    S = "ab#c"
    T = "ad#c"
    sample_array = '#a#c'

    accumulated_results = itertools.accumulate(iterable=sample_array, func=backspace_process)

    print(list(accumulated_results))

    value = backspaceCompare(S, T)
    print(value)


if __name__ == '__main__':
    main()
