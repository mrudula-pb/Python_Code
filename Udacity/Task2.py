"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from typing import List, Any

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

total_numbers = set()
for i in calls:
    total_numbers.add(i[0])
    total_numbers.add(i[1])
d1 = 0
final_dict = {}
for i in total_numbers:
    for j in calls:
        if i == j[0] or i == j[1]:
            d1 = int(j[3]) + d1
        final_dict.update({i: d1})
    d1 = 0

list1 = []
for i in final_dict:
    list1.append(final_dict[i])
max_list1 = max(list1)


def get_key(val):
    for key, value in final_dict.items():
        if val == value:
            return key


list_key = get_key(max(list1))

print(list_key + " spend the longest time, " + str(max_list1) + " seconds, on the phone during September 2016.")
