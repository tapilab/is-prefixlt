## CS 491 Undergraduate Research


## Hype Detection on Twitter
Hype -- It means that a topic may not be that popular as people considered. Instead, some companies may used bot accounts or pay for some celebrities to post tweets expressing positive attitudes towards some specific topics.

In a Chinese talk show called Morning Talk, the host, Gao Xiaosong, said that PSY and Justin Bieber are using the same company to hype their songs. Gao knows that because he is a famous producer in the Hollywood, so he may have encountered this kind of events.

Anyway, we all know that sometimes a topic pops out and immediately becomes so popular that everyone is talking about that.
So, I'm trying to find out this kind of events and hopefully I can dig out which company should be response to some particular events.

## Research Keypoints

1. Gathering data from Twitter about some specific topics. I selected 'Trump' as the keyword this time.
2. Processing the dataset and extracting out needed information. EX. Screen names and ids
3. Using the Cosine Similarity Cluster to aggregate the similar (possible hyped) tweets. 
4. Finding relatioinships from the datasets. i.e.,Is there anyone following others in this dataset?
5. Visualization on the related data.

## Related work

To be honest, I didn't find anyone doing the same research.
I did see some researches on connected account relationships on a specific topic. But it didn't help me.

## Data

Please check out the code at here: [Replicate.ipynb](Replicate.ipynb)


## Results

I found similar tweets which posted by different users. Plus, these tweets are all original tweets, which means not retweets. [Similar_Tweets.png](Similar_Tweets.png)

Moreover, there're some accounts indeed have connections and posted the similar tweets. [Related_Accounts.png](Related_Accounts.png)


## Conclusions / Future Work

The project is not finished yet, so I can not draw any further conclusions.
But for the future work, I guess the main point is visualization analysis. I mean, I've got enough data. Then I should focus on digging out the relationships and more interesting conclusions via visualization.

## 2nd Semester Results
First of all, please check out the [Hype_Detection_Yiming_Guo.pdf](Hype_Detection_Yiming_Guo.pdf). This is the report paper in IEEE format and explains everything.
In this Github repository, the codes are in Docs, and the number in front of the .py files is the order of each piece of code, and the name explains themselves.
3.3 Jacard_Similarity_Modified.py is the one returns the final result. There's 1 missing file called Relation_Real.txt, it's over the size limit of Github, I'll send you the file via email or Google Drive.
The last thing, in that 3.3 .py file, the first part of quotes is the part which being used to compute the relation pairs. The result of this part is in Jaccard1.txt. So you don't need to unquote it and run it again.

Check out the final result screen shot at here [Result.png](Result.png).

