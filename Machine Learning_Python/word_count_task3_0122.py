
class word_count:
    def word_count(self, sentence):
        # approach# 3
        for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            sentence = sentence.replace(char, '')
        sentence.lower()
        for char in '\n':
            sentence = sentence.replace(char, ' ')
        print(text.lower())

        #### b. String Manipulation: Split each word into a element in a list
        word_list = []
        word_list = sentence.split(" ")
        print(word_list)

        #### c. Count how many times each word occurs in a list using a dictionary
        dict = {}
        count = 1
        for word in word_list:
            if word not in dict:
                count = 1
                dict[word] = count
            else:
                dict[word] = dict.get(word) + 1
        print(dict)



solution = word_count()
text="""Mr. Collins returned into Hertfordshire soon after it had been quitted
by the Gardiners and Jane; but as he took up his abode with the Lucases, his arrival was no
great inconvenience to Mrs. Bennet. His marriage was now fast approaching, and she was at length
so far resigned as to think it inevitable, and even repeatedly to say, in an ill-natured tone, that
she "wished they might be happy." Thursday was to be the wedding day, and on Wednesday Miss Lucas paid
her farewell visit; and when she rose to take leave, Elizabeth, ashamed of her mother's ungracious
and reluctant good wishes, and sincerely
affected herself, accompanied her out of the room. As they went downstairs together, Charlotte said:"""
solution.word_count(text)