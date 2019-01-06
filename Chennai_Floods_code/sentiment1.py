from textblob import TextBlob
import numpy as np
import difflib
import re, string
sum=0;
i=0;
a='crocodile'
with open('n3.txt','w',encoding="utf-8") as out_file:
    file=open('Cluster0 Tweets.txt','r',encoding="utf-8")

    for line in file.readlines():
        if re.search('chembarambakkam',line,re.I):
            #print(line)
            out_file.write(line)
file.close()            

f=open('n3.txt','r',encoding="utf-8")

for line in f.readlines():
    i=i+1;
    d=line.split(',')
    tweet = re.sub(r'\$\w*','',d[2]) # Remove tickers
    tweet = re.sub(r'https?:\/\/.*\/\w*','',tweet) # Remove hyperlinks
    tweet = re.sub(r'['+string.punctuation+']+', ' ',tweet) # Remove puncutations like 's
    text=tweet
    sample=TextBlob(text)
    print(tweet)
    c=sample.sentiment.polarity;
    sum=sum+c;
    print(c)
    print("=========================================")
f.close()

    #if sample.sentiment.polarity>1:
       # print("positive")
    #elif sample.sentiment.polarity==0:
     #   print("neutral")
    #else:
     #print("negative")
d=sum/i;
print(d)
if d>1:
    print("positive")
elif d==0:
    print("neutral")
else:
    print("negative")
    

