import codecs
import numpy as np
import matplotlib.pyplot as plt
import re
import ast
content=codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*crocodile\w*"
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0
for i in content:
    matches = re.finditer(regex,i)

    for match in matches:
        if match:
            #print(i)
            if i.count('2015-12-01'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-01 00|2015-12-01 01|2015-12-01 02|2015-12-01 03',x[3])
                if temp:
                    print(x)
                    c1+=1
                temp=re.findall('2015-12-01 04|2015-12-01 05|2015-12-01 06|2015-12-01 07',x[3])
                if temp:
                    print(x)
                    c2+=1
                temp=re.findall('2015-12-01 08|2015-12-01 09|2015-12-01 10|2015-12-01 11',x[3])
                if temp:
                    print(x)
                    c3+=1
                temp=re.findall('2015-12-01 12|2015-12-01 13|2015-12-01 14|2015-12-01 15',x[3])
                if temp:
                    print(x)
                    c4+=1
                temp=re.findall('2015-12-01 16|2015-12-01 17|2015-12-01 18|2015-12-01 19',x[3])
                if temp:
                    print(x)
                    c5+=1
                temp=re.findall('2015-12-01 20|2015-12-01 21|2015-12-01 22|2015-12-01 23',x[3])
                if temp:
                    print(x)
                    c6+=1
            if i.count('2015-12-02'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-02 00|2015-12-02 01|2015-12-02 02|2015-12-02 03',x[3])
                if temp:
                    print(x)
                    c7+=1
                temp=re.findall('2015-12-02 04|2015-12-02 05|2015-12-02 06|2015-12-02 07',x[3])
                if temp:
                    print(x)
                    c8+=1
                temp=re.findall('2015-12-02 08|2015-12-02 09|2015-12-02 10|2015-12-02 11',x[3])
                if temp:
                    print(x)
                    c9+=1
                temp=re.findall('2015-12-02 12|2015-12-02 13|2015-12-02 14|2015-12-02 15',x[3])
                if temp:
                    print(x)
                    c10+=1
                temp=re.findall('2015-12-02 16|2015-12-02 17|2015-12-02 18|2015-12-02 19',x[3])
                if temp:
                    print(x)
                    c11+=1
                temp=re.findall('2015-12-02 20|2015-12-02 21|2015-12-02 22|2015-12-02 23',x[3])
                if temp:
                    print(x)
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
