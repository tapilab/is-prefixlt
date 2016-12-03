import tweepy
import time
import datetime

import json

import re
from collections import defaultdict


consumer_key="4ybgcIfZUWlcPWZmXqXC0vcrF"
consumer_secret="AgCCnpOiktrvmGjL9rFv7QvOGQ7nf70EMWzA9OZcCRs13S5k7i"
access_token="1898807028-wDFiGnKM6bOCzARxfMUSQkZl9ksEwo1YYdNVnb6"
access_token_secret="wMRQ3j6XUlWHmA6wSXOlrhWpYB7tmVGrAV5HQof7f5adn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


now = datetime.datetime.now()
i = 0
with open('Relation_Real.txt','r') as u:
    with open('Account_Created_At.json', 'a') as f:

        for tweet in u:
            list_ = []
            users = json.loads(tweet)
            for user in users:
                user = user[0]
                while True:
                    try:

                        check = api.get_user(user)
                        check = check.created_at
                        #public_tweets = api.home_timeline()

                        year_diff = now.year - check.year
                        month_diff = now.month - check.month
                        day_diff = now.day - check.day
                        age = year_diff*365 + month_diff * 30 + day_diff
                        list_.append(age)

                        if i % 50 == 0:
                            print("%dth iteration" % i)
                        i += 1
                        #a = [r._json for r in api.retweets(user[:-1])]
                        #Retweet_List = [r._json['user']['id'] for r in api.retweets(user[:-1])]
                        #f.write(json.dumps([user[:-1], Retweet_List])+'\n')
                        break
                    except tweepy.error.RateLimitError as e:

                        print("&quot ;Error on_data: %s&quot;" % str(e))
                        time.sleep(120)
                        continue
                    except tweepy.error.TweepError as te:
                        '''r = te.reason.replace('\'', '"')
                        r = json.loads(r)
                        if r[0]['code'] == 34:
                            print('got error 34 @ tweet = %s, break' % user[:-1])
                            break
                        else:
                            print("unexpected error @ tweet = %s: %s" % (user[:-1], str(te)))
                            continue'''
                        break

            f.write(json.dumps(list_))
            f.write('\n')




'''
# 这是成功的,能直接用.返回那些retweet的用户的ID
My_Tweets = api.home_timeline()
for x in My_Tweets:
    print(x)
    print('/n')
    print(type(x))
    print(x.user.id)


'''


