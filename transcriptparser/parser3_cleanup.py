import re

f = open("csv_transcript.csv", 'r')
text_lines = f.readlines()
f.close()

for line in text_lines:
    if re.match(r';', line):
        print(line)