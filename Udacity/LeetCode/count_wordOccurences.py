# Let’s say I need to count the number of word occurrences in a piece of text.

from collections import defaultdict, Counter

text = "I need to count the number of word occurrences in a piece of text. " \
       "How could I do that? Python provides us with multiple ways to do the same thing. " \
       "But only one way I find beautiful."

# word_count_dict = {}
#
# for w in text.split(' '):
#     if w in word_count_dict:
#         word_count_dict[w] += 1
#     else:
#         word_count_dict[w] = 1
# print(word_count_dict)

# using defaultdict
# word_count_dict = defaultdict(int)
# for w in text.split(' '):
#     word_count_dict[w] += 1
# print(word_count_dict)

# using counter
# word_count_dict = Counter()
# for w in text.split(' '):
#     word_count_dict[w] += 1
# print(word_count_dict)
# print(word_count_dict.most_common(3))
# print(Counter(text))

# defaultdict(list)
# s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow'), ('fruit', 'banana'), ('fruit', 'orange'),('fruit','banana')]
#
# default_dict = defaultdict(list)
#
# for k, v in s:
#     default_dict[k].append(v)
# print(default_dict)

# defaultdict(set)
s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow'), ('fruit', 'banana'), ('fruit', 'orange'),('fruit','banana')]




