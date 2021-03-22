# Code

def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    str_length = len(our_string)

    new_string = our_string.split(' ')

    for item in range(len(new_string)):
        new_string[item] = new_string[item][::-1]
        #print(new_string[item])
    return " ".join(new_string)

    '''for item in range(str_length):
        if our_string[item] == " ":
            for item_substr in range(i, item):
                new_string += our_string[item - 1 - i]
                i += 1
            new_string += " "
        else:
            continue
    print(new_string)'''


print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")