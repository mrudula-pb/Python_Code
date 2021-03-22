"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

total_count = set()

for i in texts:
    total_count.add(i[0])
    total_count.add(i[1])

for j in calls:
    total_count.add(j[0])
    total_count.add(j[1])

print("There are "+str(len(total_count)) + " different telephone numbers in the records")


