import re
from collections import defaultdict


user_tweets = defaultdict(lambda: [])
documents = open('1.txt',encoding = 'utf-8')
for line in documents:
    d = re.split('[\t\n]', line)[:4]
    user_tweets[d[1][3:]].append(d[3][6:len(d[3])-1])


for user in user_tweets:
    print(user + ": " +str(user_tweets[user]) + "\n")

t = "RT @xelerated2: @vivelafra This is a Maine trump supporter trying to caucas. Something happened there.  https://t.co/kwioEfoTRl"

for user in user_tweets:
    if t in user_tweets[user]:
	    print("Yes, it's here")

