import re

f = open("html_transcript.txt", 'r')
text = f.read()
f.close()

out_text = re.sub(r'<\/p>', '\n', text)
out_text = re.sub(r'<.*?>', '', out_text)

f = open("humanized_transcript.txt", 'w')
f.write(out_text)
