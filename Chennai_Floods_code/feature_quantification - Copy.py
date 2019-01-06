import codecs
import ast
import time
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re, string
import nltk
import pandas as pd
from datetime import datetime



def process_tweet_text(tweet):
    if tweet.startswith('@null'):
        return "[Tweet not available]"
    tweet = re.sub(r'\$\w*','',tweet) # Remove tickers
    tweet = re.sub(r'https?:\/\/.*\/\w*','',tweet) # Remove hyperlinks
    tweet = re.sub(r'['+string.punctuation+']+', ' ',tweet) # Remove puncutations like 's
    tweet = re.sub(' +',' ',tweet)
    #twtok = TweetTokenizer(strip_handles=True, reduce_len=True)

    return tweet.strip()







content=codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
##with open('original_tweet(cluster5).txt','w',encoding="utf-8") as out_file:
##    for i in content:
##        x = ast.literal_eval(i)
##        if x[0]==x[1]:
##                out_file.write(i.replace("\n",""))



c=0
count=0
time_temp=[]
regex = r"\w*crocodile\w*"
in_file=codecs.open('original_tweet(cluster2).txt','r',encoding="utf-8")
user_file=pd.read_csv('nodes.csv')
with open('dataset.csv','a+',encoding="utf-8") as out_file:
    for i in in_file:
##        matches = re.finditer(regex,i)
##        for match in matches:
##            if match:
        original_tweet=i.replace("\n","")
        try:
            x = ast.literal_eval(original_tweet)
        except:
            print("Error")
            x=None
        if len(x[2])>300:
            x=None
        if x:
            print("========================================")
            print("Computing details for ",x[2])
            cleaned_tweet=process_tweet_text(x[2])
            sample=TextBlob(cleaned_tweet)
            sentiment_score=sample.sentiment.polarity
            content.seek(0,0)
            for j in content:
                tweet = ast.literal_eval(j)
                if tweet[2]==x[2] and tweet[0]!=tweet[1]:
                    time_temp.append(tweet[3].replace("\r",""))
                    c+=1
            #user_file.seek(0,0)   
            for k in user_file.iterrows():
                if x[0]==k[1]['Label']:
                    followers=k[1]['Followers']
                    break

            matches = re.findall(regex,x[2])
            if matches:
                print("Rumour")
            else:
                print("Non Rumour")
            print("No of reteets",c)
            print("No of followers of user",followers)
            print("Sentimentality Scores",sentiment_score)
            if time_temp:
                min_time=datetime.strptime(min(time_temp), '%Y-%m-%d %H:%M:%S')
                max_time=datetime.strptime(max(time_temp), '%Y-%m-%d %H:%M:%S')
                original_time=x[3].replace("\r","")
                original_time=datetime.strptime(original_time, '%Y-%m-%d %H:%M:%S')
                first_retweet=(((min_time-original_time).total_seconds())/60)/60
                persistance_time=(((max_time-original_time).total_seconds())/60)/60
                print("Time of first retweet",first_retweet)
                print("Time for which the tweet persisted in network",persistance_time)
                if matches:
                    out_file.write(str(c)+","+str(followers)+","+str(sentiment_score)+","+str(first_retweet)+","+str(persistance_time)+","+"Rumour"+"\n")
                else:
                    out_file.write(str(c)+","+str(followers)+","+str(sentiment_score)+","+str(first_retweet)+","+str(persistance_time)+","+"Non-Rumour"+"\n")
            else:
                if matches:
                    out_file.write(str(c)+","+str(followers)+","+str(sentiment_score)+","+"0"+","+"0"+","+"Rumour"+"\n")
                else:
                    out_file.write(str(c)+","+str(followers)+","+str(sentiment_score)+","+"0"+","+"0"+","+"Non-Rumour"+"\n")
                
            c=0
            time_temp=[]
            count+=1
            print("Count",count)
            with open("filecount.txt","w+") as f:
                    f.write(str(count))
