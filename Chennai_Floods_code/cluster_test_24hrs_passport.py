import codecs
import numpy as np
import matplotlib.pyplot as plt
import re
import ast
content=codecs.open('Cluster5 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*passport\w*"
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0
for i in content:
    matches = re.finditer(regex,i)

    for match in matches:
        if match:
            #print(i)
            if i.count('2015-12-07'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-07 00|2015-12-07 01|2015-12-07 02|2015-12-07 03',x[3])
                if temp:
                    c1+=1
                temp=re.findall('2015-12-07 04|2015-12-07 05|2015-12-07 06|2015-12-07 07',x[3])
                if temp:
                    c2+=1
                temp=re.findall('2015-12-07 08|2015-12-07 09|2015-12-07 10|2015-12-07 11',x[3])
                if temp:
                    c3+=1
                temp=re.findall('2015-12-07 12|2015-12-07 13|2015-12-07 14|2015-12-07 15',x[3])
                if temp:
                    c4+=1
                temp=re.findall('2015-12-07 16|2015-12-07 17|2015-12-07 18|2015-12-07 19',x[3])
                if temp:
                    c5+=1
                temp=re.findall('2015-12-07 20|2015-12-07 21|2015-12-07 22|2015-12-07 23',x[3])
                if temp:
                    c6+=1
            if i.count('2015-12-08'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-08 00|2015-12-08 01|2015-12-08 02|2015-12-08 03',x[3])
                if temp:
                    c7+=1
                temp=re.findall('2015-12-08 04|2015-12-08 05|2015-12-08 06|2015-12-08 07',x[3])
                if temp:
                    c8+=1
                temp=re.findall('2015-12-08 08|2015-12-08 09|2015-12-08 10|2015-12-08 11',x[3])
                if temp:
                    c9+=1
                temp=re.findall('2015-12-08 12|2015-12-08 13|2015-12-08 14|2015-12-08 15',x[3])
                if temp:
                    c10+=1
                temp=re.findall('2015-12-08 16|2015-12-08 17|2015-12-08 18|2015-12-08 19',x[3])
                if temp:
                    c11+=1
                temp=re.findall('2015-12-08 20|2015-12-08 21|2015-12-08 22|2015-12-08 23',x[3])
                if temp:
                    c12+=1

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
print(c11)
print(c12)

fig, ax=plt.subplots()
index=np.arange(10)
bar_width=0.15
opacity=0.9

belief=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)
y=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(y,belief)
plt.show()

rects1=plt.bar(index,belief,bar_width,alpha=opacity,color='b',label='Tweets')
plt.xlabel('time')
plt.ylabel('no. of tweets')
plt.title('Temporal feature of rumor analysis')
plt.xticks(index+(0.5*bar_width),('1Dec','2Dec','3Dec','4Dec','5Dec','6Dec','7Dec','8Dec','9Dec','10Dec'))
plt.legend()
plt.tight_layout()
plt.show()
