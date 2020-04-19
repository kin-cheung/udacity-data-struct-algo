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


first_record = texts[0]
first_record_timestamp = texts[0][2]
for text in texts[1:] :
    if text[2] < first_record_timestamp :
        first_record_timestamp = text[2]
        first_record = text

last_record = calls[0]
last_record_timestamp = calls[0][2]
for call in calls[1:] :
    if call[2] > last_record_timestamp :
        last_record_timestamp = call[2]
        last_record = call

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print('First record of texts,', first_record[0], 'texts', first_record[1], 'at time', first_record[2])
print('Last record of calls,', last_record[0], 'calls', last_record[1], 'at time', last_record[2], 'lasting', last_record[3], 'seconds')
