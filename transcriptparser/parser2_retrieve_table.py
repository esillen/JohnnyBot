import re

ACTORS = ("Johnny", "Lisa", "Mark", "Denny", "Peter", "Mike", "Claudette", "Michelle")

f = open("humanized_transcript.txt", 'r')
text_lines = f.readlines()
f.close()

out_lines = []

for line in text_lines:
    stuff = line.split(':')
    if len(stuff) != 2:
        continue
    if stuff[0] in ACTORS:
        stuff[1] = re.sub(r'\(.*?\)', '', stuff[1])  # remove parentheses
        lines = re.findall(r'.*?[.?!]', stuff[1])
        for a_line in lines:
            out_lines.append(';'.join((stuff[0], a_line)))
    else:
        print("actor %s found" % (stuff[0]))
print(out_lines)
f = open("csv_transcript.csv", 'w')
f.write('\n'.join(out_lines))
f.close()
