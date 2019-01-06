import codecs
import numpy as np
import matplotlib.pyplot as plt
import re
import ast
content=codecs.open('Cluster3 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*little girl\w*"
c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0
for i in content:
    matches = re.finditer(regex,i)

    for match in matches:
        if match:
            #print(i)
            if i.count('2015-12-04'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-04 00|2015-12-04 01|2015-12-04 02|2015-12-04 03',x[3])
                if temp:
                    c1+=1
                temp=re.findall('2015-12-04 04|2015-12-04 05|2015-12-04 06|2015-12-04 07',x[3])
                if temp:
                    c2+=1
                temp=re.findall('2015-12-04 08|2015-12-04 09|2015-12-04 10|2015-12-04 11',x[3])
                if temp:
                    c3+=1
                temp=re.findall('2015-12-04 12|2015-12-04 13|2015-12-04 14|2015-12-04 15',x[3])
                if temp:
                    c4+=1
                temp=re.findall('2015-12-04 16|2015-12-04 17|2015-12-04 18|2015-12-04 19',x[3])
                if temp:
                    c5+=1
                temp=re.findall('2015-12-04 20|2015-12-04 21|2015-12-04 22|2015-12-04 23',x[3])
                if temp:
                    c6+=1
            if i.count('2015-12-05'):
                x = ast.literal_eval(i)
                temp=re.findall('2015-12-05 00|2015-12-05 01|2015-12-05 02|2015-12-05 03',x[3])
                if temp:
                    c7+=1
                temp=re.findall('2015-12-05 04|2015-12-05 05|2015-12-05 06|2015-12-05 07',x[3])
                if temp:
                    c8+=1
                temp=re.findall('2015-12-05 08|2015-12-05 09|2015-12-05 10|2015-12-05 11',x[3])
                if temp:
                    c9+=1
                temp=re.findall('2015-12-05 12|2015-12-05 13|2015-12-05 14|2015-12-05 15',x[3])
                if temp:
                    c10+=1
                temp=re.findall('2015-12-05 16|2015-12-05 17|2015-12-05 18|2015-12-05 19',x[3])
                if temp:
                    c11+=1
                temp=re.findall('2015-12-05 20|2015-12-05 21|2015-12-05 22|2015-12-05 23',x[3])
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
