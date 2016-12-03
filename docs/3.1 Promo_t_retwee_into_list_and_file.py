import tweepy
import networkx as nx
import matplotlib
import json
import time


import re
from collections import defaultdict

consumer_key="4ybgcIfZUWlcPWZmXqXC0vcrF"
consumer_secret="AgCCnpOiktrvmGjL9rFv7QvOGQ7nf70EMWzA9OZcCRs13S5k7i"
access_token="1898807028-wDFiGnKM6bOCzARxfMUSQkZl9ksEwo1YYdNVnb6"
access_token_secret="wMRQ3j6XUlWHmA6wSXOlrhWpYB7tmVGrAV5HQof7f5adn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

'''
Retweeters = []
with open('Promoted_Tweets_ID_Retweets.json', 'r') as f:
    for each in f:
        content = json.loads(each)
        #print(content[1])
        for e in content[1]:
            Retweeters.append(e)

print(Retweeters)

# 从这里开始是从2.6 NX copy过来的
# 但是已经修改过了!!!


for user in Retweeters:
    while True:
        try:
            with open('Relation.txt', 'a') as f:
                friend_list = api.friends_ids(user)
                print(friend_list)
                l = json.dumps([user, friend_list])
                f.write(l)
                f.write('\n')
                break
        except tweepy.error.RateLimitError as e:

            print("&quot ;Error on_data: %s&quot;" % str(e))
            time.sleep(120)
            continue
        except tweepy.error.TweepError as te:
            r = te.reason.replace('\'', '"')
            r = json.loads(r)
            if r[0]['code'] == 34:
                print('got error 34 @ tweet = %s, break' % user[:-1])
                break
            else:
                print("unexpected error @ tweet = %s: %s" % (user[:-1], str(te)))
'''


Retweeters = []
# Promoted_Tweets_ID_Retweets
with open('Promoted_Tweets_ID_Retweets_10.json', 'r') as f:
    for each in f:
        content = json.loads(each)
        #print(content[1])
        Retweeters.append(content[1])

print(Retweeters)

#不写了
# relation 8.5 是因为8出错了,所以可能有一半数据没记录全.重新记录一次
with open('Relation_10.txt', 'a') as f:

    for users in Retweeters:
        users_ = []
        for user in users:
            while True:
                try:
                    friend_list = api.friends_ids(user)
                    follower_list = api.followers_ids(user)
                    print(friend_list)
                    #l = json.dumps([user, friend_list, follower_list])
                    break
                except tweepy.error.RateLimitError as e:

                    print("&quot ;Error on_data: %s&quot;" % str(e))
                    time.sleep(120)
                    continue
                except tweepy.error.TweepError as te:
                    #r = te.reason.replace('\'', '"')
                    print(te.reason)
                    break
                except:
                    print("Unexpected error raised @ %s" % user)
                    break
                    '''r = json.loads(te.reason)
                    if r[0]['code'] == 34:
                        print('got error 34 @ tweet = %s, break' % user[:-1])
                        break
                    else:
                        print("unexpected error @ tweet = %s: %s" % (user[:-1], str(te)))
                        break'''
            users_.append([user, friend_list, follower_list])
        l = json.dumps(users_)
        f.write(l+'\n')
        f.flush()
        # 似乎是缩进的问题,原本是在这个位置


