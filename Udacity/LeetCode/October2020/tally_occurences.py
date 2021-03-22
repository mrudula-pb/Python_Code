
from collections import Counter
# Tally occurrences of words in a list
cnt = Counter()
dct = {}
lst = ['red', 'blue', 'red', 'green', 'blue', 'blue']
for word in lst:
    cnt[word] += 1
print(cnt)

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open(''))
