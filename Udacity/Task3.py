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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""Part A"""

total_numbers = []
total_numbers1 = set()
for i in calls:
    ss = i[0]
    rr = i[1]
    if ss[:5] == '(080)':
        if '(0' in rr:
            total_numbers.append(rr.split(')')[0][1:])
        elif '' in rr:
            total_numbers.append(rr.split()[0])
        elif rr[:3] == '140':
            total_numbers.append(rr[:3])
for ii in total_numbers:
    total_numbers1.add(ii)
total_call_count = 0
total_calls = len(total_numbers)
for i in total_numbers:
    if i == '080':
        total_call_count += 1
value = (total_call_count / total_calls) * 100

print("The numbers called by people in Bangalore have codes:")
for i in sorted(total_numbers1):
    print(i)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(value))