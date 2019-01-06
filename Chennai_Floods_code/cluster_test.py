import codecs
import numpy as np
import matplotlib.pyplot as plt
import re
content=codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*crocodile\w*"
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=0
for i in content:
    matches = re.finditer(regex,i)
    for match in matches:
        print(match)
        if match:
            print(i)
            if i.count('2015-04-25'):
                #print(i)
                c1+=1
            if i.count('2015-04-26'):
                c2+=1
            if i.count('2015-04-27'):
                c3+=1
            if i.count('2015-04-28'):
                c4+=1
            if i.count('2015-04-29'):
                c5+=1
            if i.count('2015-04-30'):
                c6+=1
            if i.count('2015-05-01'):
                #print(i)
                c7+=1
            if i.count('2015-05-02'):
                c8+=1
            if i.count('2015-05-03'):
                c9+=1
            if i.count('2015-05-04'):
                c10+=1

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)
print(c10)

fig, ax=plt.subplots()
index=np.arange(11)
bar_width=0.15
opacity=0.9

belief=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
y=[1,2,3,4,5,6,7,8,9,10]
plt.xlabel('Time')
plt.ylabel('No. of tweets')
plt.xticks(index+(6.6*bar_width),('1Dec','2Dec','3Dec','4Dec','5Dec','6Dec','7Dec','8Dec','9Dec','10Dec'))
plt.plot(y,belief,'bo',linestyle='-')
plt.show()

rects1=plt.bar(index,belief,bar_width,alpha=opacity,color='b',label='Tweets')
plt.xlabel('Time')
plt.ylabel('No. of tweets')
plt.title('Temporal feature of rumor analysis')
plt.xticks(index+(0.5*bar_width),('1Dec','2Dec','3Dec','4Dec','5Dec','6Dec','7Dec','8Dec','9Dec','10Dec'))
plt.legend()
plt.tight_layout()
plt.show()
