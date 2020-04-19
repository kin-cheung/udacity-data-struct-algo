"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

time_spent = {}
longest_spent_number = None
longest_spent = 0
for call in calls :
    caller_spent = time_spent.get(call[0], 0)
    time_spent[call[0]] = caller_spent + int(call[3])
    if (time_spent[call[0]] > longest_spent) :
        longest_spent_number = call[0]
        longest_spent = time_spent[call[0]]        
    
    callee_spent = time_spent.get(call[1], 0)
    time_spent[call[1]] = callee_spent + int(call[3])
    if (time_spent[call[1]] > longest_spent) :
        longest_spent_number = call[1]
        longest_spent = time_spent[call[1]]   
        
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
print(longest_spent_number, 'spent the longest time,', longest_spent ,'seconds,', 'on the phone during September 2016.')


