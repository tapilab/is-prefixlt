import tweepy
import networkx as nx
import json
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


total = []

'''
with open('Relation.txt') as r:
    graph = nx.Graph()
    a = r.readline()
    e = json.loads(a)
    retweeters = [w[0] for w in e]
    friends = [x for x in [w[1] for w in e]]
    followers = [x for x in [w[2] for w in e]]
    for ret in retweeters:
        if ret in friends or ret in followers:
            print(1)
    for w in e:
        rt = w[0]
        fr = w[1]
        fo = w[2]
        graph.add_edges_from([(rt, u) for u in fr + fo])
    print(nx.average_clustering(graph))


'''
# File Relation_8.5, Relation 这两个都是promoted.
# File Relation_Real, 还有将来的后面加数字的,都是Genuine

with open('Relation_Total.txt') as r:
    for each_list in r:
        retweeter = []
        friends = []
        the_person_being_followed=[]
        graph = nx.Graph()

        extract = json.loads(each_list)
        #print(extract)
        #print('Look upper')
        #print(type(extract))
        #print(extract[1])


        retweeters_ = [w[0] for w in extract]
        friends_ = list(np.concatenate([w[1] for w in extract]))
        followers_ = list(np.concatenate([x for x in [w[2] for w in extract]]))
        n = 0
        for ret_ in retweeters_:
            if ret_ in friends_ or ret_ in followers_:
                n += 1
        print(n)


        for e in extract:
            retweeter = str(e[0])
            friends = [str(r) for r in e[1]]
            the_person_being_followed = [str(r) for r in e[2]]

            graph.add_edges_from([(retweeter, u) for u in friends + the_person_being_followed])
            '''
            related_rts = [r for r in retweeters_ if r in friends+the_person_being_followed]
            graph.add_edges_from([(retweeter, u) for u in related_rts])
            graph.add_edges_from([(retweeter, 0)])
            '''
        clustering_coefficient = nx.average_clustering(graph)
        total.append(clustering_coefficient)
        print(clustering_coefficient)
    print(total)

s_total = sorted(total)
plt.plot(range(len(s_total)), s_total, 'bo-')
plt.show()


'''
# 这一块内容是旧版的,暂时不需要了
with open('Relation.txt') as r:
    for each_list in r:
        extract = json.loads(each_list)
        #print(extract)
        #print(type(extract))
        #print(extract[1])

        retweeter.append(str(extract[0]))
        friends.append([str(r) for r in extract[1]])
# 这里开始是打开第二个文件,导入另一组列表
with open('Relation_Followers_ids.txt') as r:
    for each_list in r:
        extract = json.loads(each_list)
        #print(extract)
        #print(type(extract))
        #print(extract[1])

        #retweeter.append(extract[0])
        the_person_being_followed.append([str(r) for r in extract[1]])
'''


'''
graph = nx.Graph()
n = 0
end = len(retweeter)
'''

#print(set([r for r in retweeter if r in np.concatenate(friends)]))
#print(set([r for r in retweeter if r in np.concatenate(the_person_being_followed)]))

#set_friends = list(set([r for r in retweeter if r in np.concatenate(friends)]))
#set_the_person_being_followed = list(set([r for r in retweeter if r in np.concatenate(the_person_being_followed)]))



'''
# 这个是network x 的方法,现在用统计图,不用这部分了
graph = nx.Graph()

i = 0
while i<len(retweeter):
    for id in friends[i]:
        graph.add_edges_from([(retweeter[i], id)])
    for id in the_person_being_followed[i]:
        graph.add_edges_from([(retweeter[i], id)])
    i+=1
'''




#print(nx.average_clustering(graph))

# 别画图了,每次都卡死……
#nx.draw(graph, with_labels=False)

# This figure is for #Blizzcon.
#Clustering coefficient


plt.hist(total, bins=10, range=None, normed=False)

plt.show()
