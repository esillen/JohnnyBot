import tkinter as tk
import random

ACTORS = ("Johnny", "Lisa", "Mark", "Denny", "Peter", "Mike", "Claudette", "Michelle")

class ActorLine:
    def __init__(self, character, line, about_user=False, topics={}):
        self.character = character
        self.line = line
        self.about_user = about_user
        self.topics = topics
        self.recently_tagged = False

    def __str__(self):
        return ';'.join(self.character, self.line, self.about_user, self.topics, ','.join(self.recently_tagged.keys()))

f = open('tagged_transcript.csv', 'r')
text_lines = f.readlines()
f.close()

actor_lines = []

for line in text_lines:
    stuff = line.split(';')
    if len(stuff) == 2:
        actor_lines.append(ActorLine(stuff[0], stuff[1]))
    elif len(stuff) == 4:
        actor_lines.append(ActorLine(stuff[0], stuff[1], stuff[2], stuff[3].split(',')))

# add user name
#regex = "(" + ")|(".join(ACTORS) + ")"
#a_line = re.sub(regex, '<USER_NAME>', a_line)



current_actor_line = random.choice(actor_lines)


def write_to_file():
    f = open('tagged_transcript.csv', 'w')
    f.write('\n'.join([str(x) for x in actor_lines]))
    f.close()


def get_untagged_actor_line():
    global current_actor_line
    for i in range(1000):
        a_line = random.choice(actor_lines)
        if not a_line.recently_tagged:
            break
    current_actor_line = a_line


def tag_actor_line(topic):
    current_actor_line.topics[topic] = True
    current_actor_line.recently_tagged = True

root = tk.Tk()
#Frames
topics_frame = tk.Frame(root)
text_frame = tk.Frame(root)
buttons_frame = tk.Frame(root)

#Buttons
b1 = tk.Button(topics_frame, text="girls", command=lambda: tag_actor_line('girls'))
b2 = tk.Button(topics_frame, text="laughter", command=lambda: tag_actor_line('laughter'))
b3 = tk.Button(topics_frame, text="aggression", command=lambda: tag_actor_line('aggression'))
b4 = tk.Button(topics_frame, text="sadness", command=lambda: tag_actor_line('sadness'))
b5 = tk.Button(topics_frame, text="deep", command=lambda: tag_actor_line('deep'))
b6 = tk.Button(topics_frame, text="confirmation", command=lambda: tag_actor_line('confirmation'))

next_button = tk.Button(buttons_frame, text="NEXT", command=get_untagged_actor_line)
save_button = tk.Button(buttons_frame, text="NEXT", command=write_to_file)

for thing in (topics_frame, text_frame, b1, b2, b3, b4, b5, b6):
    thing.pack()

root.mainloop()