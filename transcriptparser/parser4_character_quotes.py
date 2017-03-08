import re

f = open("csv_transcript.csv", 'r')
text_lines = f.readlines()
f.close()

out_lines = []

for line in text_lines:
    stuff = line.split(r';')
    if stuff[0] == "Johnny":
        out_lines.append(stuff[1])


f = open("johnny_script.csv", "w")
f.writelines(out_lines)
f.close()