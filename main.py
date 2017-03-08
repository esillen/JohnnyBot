import random, re


f = open("transcriptparser/johnny_script.csv", 'r')
quotes = f.readlines()
f.close()

user_name = input("Enter your name: ")
user_reply = ""
user_replies = {}
while user_reply != "BAJS":
    reply = random.choice(quotes)
    reply = re.sub(r'<USER_NAME>', user_name, reply)
    user_reply = input(reply)
    user_replies[user_reply] = True

f = open("topics.txt", 'w')
f.write('\n'.join(user_replies.keys()))
f.close()