import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math as math
import scipy.special as sp

from textblob import TextBlob
import numpy as np
import difflib
import re
import ast
sum=0;
i=0;
var=[]

#a='crocodile'
with open('n3.txt','w',encoding="utf-8") as out_file:
    file=open('Cluster5 Tweets.txt','r',encoding="utf-8")

    for line in file.readlines():
        if re.search('passport',line,re.I):
            #print(line)
            out_file.write(line)
file.close()            


f=open('n3.txt','r',encoding="utf-8")

temp=[]
for line in f.readlines():
    
    text = ast.literal_eval(line)
    if text[3]<='2015-12-05 23:59:59':
        #print(text[3])
        text=text[2]
        #print(text)
        sample=TextBlob(text);
        word=line.split(",")
        #print(sample)
        #print(word[2])
        c=sample.sentiment.polarity;
        var.append(c);
        i=i+1;
        if c<0:
        #print(c)
            temp.append([word[2],c])
        #c=sample;
        sum=sum+c;
        #print(c)
        #print("=========================================")

print(temp)
print(i)
print(var)
a=len(var)
print(a)
f.close()
d=sum/i;
print(d)
# create data

alpha   = np.linspace(0,len(var),len(var))
#a=len(var)
#print(a)
omega = 2*np.pi/len(var)


def func(alpha, a1, ac2, ac3, ac4, ac5, ac6, ac7):
    fit     = a1 + ac2*np.sin(omega*alpha) + ac3*np.sin(omega*2*alpha) + ac4*np.sin(omega*3*alpha) + ac5*np.sin(omega*4*alpha) +      ac6*np.sin(omega*5*alpha) + ac7*np.sin(omega*6*alpha)
    return fit

popt, pcov = curve_fit(func, alpha, var) 

print (popt)

y_fit= func(alpha,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6])

plt.plot(alpha,var,'bo',label='discrete data')
plt.plot(alpha,y_fit,'r',label='periodic fit')
plt.ylabel('Sentiment Score of Tweet')
plt.xlabel('No. of Tweets')
plt.legend()
plt.show()
