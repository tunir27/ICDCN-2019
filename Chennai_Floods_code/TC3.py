import codecs
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re, string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans,DBSCAN
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn import metrics
import numpy as np
import pandas as pd
import networkx as nx

df = pd.read_csv('edges.csv',lineterminator='\n')
dn= pd.read_csv('nodes.csv')
##corpus = codecs.open('Output1.txt', mode="r", encoding="utf-8")
##with pd.HDFStore('Output.hdf') as store:
##   df=store['test']

##lines = corpus.read().lower().split("\n")
print("Reading Done")
print(len(df))
stopwords=stopwords.words('english')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
def process_tweet_text(tweet):
   if tweet.startswith('@null'):
       return "[Tweet not available]"
   tweet = re.sub(r'\$\w*','',tweet) # Remove tickers
   tweet = re.sub(r'https?:\/\/.*\/\w*','',tweet) # Remove hyperlinks
   tweet = re.sub(r'['+string.punctuation+']+', ' ',tweet) # Remove puncutations like 's
   twtok = TweetTokenizer(strip_handles=True, reduce_len=True)
   tokens = twtok.tokenize(tweet)
   tokens = [i.lower() for i in tokens if i not in stopwords and len(i) > 2 and  
                                             i in english_vocab]
   return tokens


vectors = []
dup_rem_tweet=[]
c=0
#duplicate_dict = {}
used_lines = []
i=0

##for t in df.iterrows():
##   print(t[1]['Time'])
print("Starting vectors loop")
for t in df.iterrows():
   time=t[1]['Time\r']
   tweet=t[1]['Text']
   sor=t[1]['Source']
   tar=t[1]['Target']
   tweet = tweet.lower()
   c=c+1
   print(i)
##   if c>=2000:
##      break
##   if i % 2 == 0 and tweet not in duplicate_dict:
##      duplicate_dict[tweet] = True
   used_lines.append([sor,tar,tweet,time])
   vectors.append(process_tweet_text(tweet))
   i+=1

#print(len(used_lines))
print("Ending vectors loop")

print("Starting cleaned tweets loop")
cleaned_tweets = []
for tw in vectors:
    words = tw
    cleaned_tweet = " ".join(w for w in words if len(w) > 2 and w.isalpha()) #Form sentences of processed words
    cleaned_tweets.append(cleaned_tweet)

print("Ending cleaned tweets loop")
##with open("cleaned.txt", "w+") as text_file:
##   for i in cleaned_tweets:
##      text_file.write(i+"\n")
##
##print("Writing done")


print("Starting tdidf")
tfidf_vectorizer = TfidfVectorizer(use_idf=True, ngram_range=(1,3))  
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_tweets)  
feature_names = tfidf_vectorizer.get_feature_names() # num phrases   
#dist = 1 - cosine_similarity(tfidf_matrix)  

print("tdidf done")

print("starting clusterer")
num_clusters = 10
km = KMeans(n_clusters=num_clusters)  
km.fit(tfidf_matrix)  
clusters = km.labels_.tolist()

print("clustering done")

def ClusterIndicesNumpy(clustNum, labels_array): #numpy 
    return np.where(labels_array == clustNum)[0]
temp=[]
for i in range(num_clusters):
   print("For Cluster",i)
   fnamet="Cluster"+str(i)+" Tweets.txt"
   fnameh="Cluster"+str(i)+" Tweets.hdf"
   with open(fnamet, "w+", encoding="utf-8") as text_file:
   #print(len(ClusterIndicesNumpy(i,km.labels_)))
      for j in ClusterIndicesNumpy(i,km.labels_):
         text_file.write(str(used_lines[j])+"\n")
         temp.append(used_lines[j])
         #print(used_lines[j])
   #df1 = pd.DataFrame(temp,columns=['Source','Target','Tweet','Time'])
   #df1.to_hdf(fnameh,'test',format='table',mode='w')
   print("Writing done")   
##silhouette_avg = metrics.silhouette_score(tfidf_matrix, clusters, metric='cosine')
##print("For n_clusters = ", num_clusters, "The average silhouette_score is: ", silhouette_avg)
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    print("Cluster {} : Words :".format(i))
    for ind in order_centroids[i, :10]: 
        print(' %s' % feature_names[ind])
         

##from gensim import corpora, models,similarities
##from nltk.corpus import stopwords
##from nltk.stem.wordnet import WordNetLemmatizer
##import string
##stop = set(stopwords.words('english'))
##exclude = set(string.punctuation)
##lemma = WordNetLemmatizer()
##def clean(doc):
##    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
##    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
##    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
##    return normalized
##texts = [text for text in cleaned_tweets if len(text) > 2]
##doc_clean = [clean(doc).split() for doc in texts]
##dictionary = corpora.Dictionary(doc_clean)
##doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
##ldamodel = models.ldamodel.LdaModel(doc_term_matrix, num_topics=6, id2word = dictionary, passes=5)
##similar_index = similarities.MatrixSimilarity(ldamodel[doc_term_matrix])
##print(similar_index)
##for topic in ldamodel.show_topics(num_topics=6, formatted=False, num_words=6):
##    print("Topic {}: Words: ".format(topic[0]))
##    topicwords = [w for (w, val) in topic[1]]
##    print(topicwords)


##import gensim
##from gensim.models.doc2vec import TaggedDocument
##taggeddocs = []
##tag2tweetmap = {}
##for index,i in enumerate(cleaned_tweets):
##    if len(i) > 2: # Non empty tweets
##        tag = u'SENT_{:d}'.format(index)
##        sentence = TaggedDocument(words=gensim.utils.to_unicode(i).split(),tags=[tag])
##        tag2tweetmap[tag] = i
##        taggeddocs.append(sentence)
##model = gensim.models.Doc2Vec(vector_size=100, dbow_words= 1, dm=0, epochs=1,  window=5, seed=1337, min_count=5, workers=4,alpha=0.025, min_alpha=0.025)
##model.build_vocab(taggeddocs)
##for epoch in range(60):
##    if epoch % 20 == 0:
##        print('Now training epoch %s' % epoch)
##    model.train(taggeddocs, total_examples=len(taggeddocs), epochs=1)
##    model.alpha -= 0.002  # decrease the learning rate
##    model.min_alpha = model.alpha  # fix the learning rate, no decay
##
##from sklearn.cluster import KMeans
##dataSet = model.wv.syn0
##print(model.docvecs[0])
##kmeansClustering = KMeans(n_clusters=6)
##centroidIndx = kmeansClustering.fit_predict(dataSet)
##topic2wordsmap = {}
##for i, val in enumerate(dataSet):
##   tag = model.docvecs.index_to_doctag(i)
##   topic = centroidIndx[i]
##   if topic in topic2wordsmap.keys():
##      for w in (tag2tweetmap[tag].split()):
##          topic2wordsmap[topic].append(w)
##   else:
##       topic2wordsmap[topic] = []
##for i in topic2wordsmap:
##    words = topic2wordsmap[i]
##    print("Topic {} has words {}".format(i, words[:5]))
##
##for i in range(6):
##   print("For Cluster",i)
##   print(len(ClusterIndicesNumpy(i,kmeansClustering.labels_)))
##   #for j in ClusterIndicesNumpy(i,km.labels_):
##      #print(used_lines[j])
##   print("===========================================")
