from itertools import permutations, combinations


def first_recur_char(characters):
    combo = combinations(characters, 2)

    for i in list(combo):
        print(i[0], i[1])
        if i[0] == i[1]:
            print(i[0])
            exit()


def main():
    characters = ['B', 'C', 'C', 'B']
    first_recur_char(characters)


if __name__ == '__main__':
    main()

