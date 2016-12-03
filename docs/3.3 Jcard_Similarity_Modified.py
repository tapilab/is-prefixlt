
import json
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import KFold


total = []


# File Relation_8.5, Relation 这两个都是promoted.
# File Relation_Real, 还有将来的后面加数字的,都是Genuine
'''
def calc_sim(extract):
    all_friends_sim = []
    all_followers_sim = []
    all_relations_sim = []
    for i in range(len(extract)-1):
        for j in range(i+1, len(extract)):
            friends_i = [str(r) for r in extract[i][1]]
            friends_j = [str(r) for r in extract[j][1]]
            followers_i = [str(r) for r in extract[i][2]]
            followers_j = [str(r) for r in extract[j][2]]
            friends_sim = (len([r for r in friends_i if r in friends_j])+1) / (len(set(friends_i+friends_j))+1)
            followers_sim = (len([r for r in followers_i if r in followers_j])+1) / (len(set(followers_i+followers_j))+1)
            relations_sim = (len([r for r in set(friends_i+followers_i) if r in set(friends_j+followers_j)])+1) / (len(set(friends_i+friends_j+followers_i+followers_j))+1)
            all_friends_sim.append(friends_sim)
            all_followers_sim.append(followers_sim)
            all_relations_sim.append(relations_sim)
    return [all_friends_sim, all_followers_sim, all_relations_sim]

data_x, data_y = [], []
raw_data_x = []
for filename in ['Relation_8.5.txt', 'Relation_9.txt', 'Relation_10.txt', 'Relation_Real.txt']:
    with open(filename, 'r') as r:
        for each_list in r:
            #print('running')
            data = []
            extract = json.loads(each_list)
            print(len(extract))
            friends_sim, followers_sim, relations_sim = calc_sim(extract)
            friends_sim = sorted(friends_sim)
            followers_sim = sorted(followers_sim)
            relations_sim = sorted(relations_sim)
            raw_data_x.append([friends_sim, followers_sim, relations_sim])
            data += [friends_sim[0], friends_sim[-1], np.mean(friends_sim), friends_sim[int(len(friends_sim)/10)], friends_sim[int(len(friends_sim)*9/10)],
                     followers_sim[0], followers_sim[-1], np.mean(followers_sim), followers_sim[int(len(followers_sim)/10)], followers_sim[int(len(followers_sim)*9/10)],
                     relations_sim[0], relations_sim[-1], np.mean(relations_sim), relations_sim[int(len(relations_sim)/10)], relations_sim[int(len(relations_sim)*9/10)]]
            data_x.append(data)
            if filename == 'Relation_Real.txt':
                data_y.append(1)
            else:
                data_y.append(0)

with open("jaccard1.txt", 'w') as f:
    f.write(json.dumps(data_x)+'\n')
    f.write(json.dumps(data_y)+'\n')
    f.write(json.dumps(raw_data_x)+'\n')
'''

with open("jaccard1.txt", 'r') as f:
    data_x = json.loads(f.readline())
    data_y = json.loads(f.readline())

data_y = [0 if r ==1 else 1 for r in data_y]

data_x_1 = []
with open("Account_Created_At.json", 'r') as u:
    for line in u:
        ages = json.loads(line)
        mean = np.mean(ages)
        std = np.std(ages)
        data_x_1.append([mean, std])
data_x = [data_x[i]+data_x_1[i] for i in range(len(data_x))]



lr = LogisticRegression(random_state=0)
rf = RandomForestClassifier(random_state=0)

results = []

kf = KFold(n_splits=4, shuffle=True, random_state=0)
for train_index, test_index in kf.split(data_x):
    train_data = np.array(data_x)[train_index]
    train_target = np.array(data_y)[train_index]
    test_data = np.array(data_x)[test_index]
    test_target = np.array(data_y)[test_index]
    rf.fit(train_data, train_target)
    prediction = rf.predict(test_data)
    results.append([accuracy_score(test_target, prediction), precision_score(test_target, prediction), recall_score(test_target, prediction), f1_score(test_target, prediction), roc_auc_score(test_target, prediction)])
    print(accuracy_score(test_target, prediction), precision_score(test_target, prediction), recall_score(test_target, prediction), f1_score(test_target, prediction), roc_auc_score(test_target, prediction))

print(results)
results = (np.mean([r[0] for r in results]), np.mean([r[1] for r in results]), np.mean([r[2] for r in results]), np.mean([r[3] for r in results]), np.mean([r[4] for r in results]))
print("Accuracy:\t%0.4f\nPrecision:\t%0.4f\nRecall:\t%0.4f\nF1 score:\t%0.4f\nAUC of ROC:\t%0.4f\n" % results)

print(rf.feature_importances_)

'''
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

            related_rts = [r for r in retweeters_ if r in friends+the_person_being_followed]
            graph.add_edges_from([(retweeter, u) for u in related_rts])
            graph.add_edges_from([(retweeter, 0)])

        clustering_coefficient = nx.average_clustering(graph)
        total.append(clustering_coefficient)
        print(clustering_coefficient)
'''


'''
Top 3 Critria:
10th quantile of friends similarity
mean of followers similarity
mean of retweeters account age
'''