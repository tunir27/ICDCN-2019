import codecs
import numpy as np
import matplotlib.pyplot as plt
import re
import ast
##content=codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
##regex = r"\w*crocodile\w*"
##c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0
##for i in content:
##    matches = re.finditer(regex,i)
##
##    for match in matches:
##        if match:
##            #print(i)
##            if i.count('2015-12-01'):
##                x = ast.literal_eval(i)
##                temp=re.findall('2015-12-01 00|2015-12-01 01|2015-12-01 02|2015-12-01 03',x[3])
##                if temp:
##                    c1+=1
##                temp=re.findall('2015-12-01 04|2015-12-01 05|2015-12-01 06|2015-12-01 07',x[3])
##                if temp:
##                    c2+=1
##                temp=re.findall('2015-12-01 08|2015-12-01 09|2015-12-01 10|2015-12-01 11',x[3])
##                if temp:
##                    c3+=1
##                temp=re.findall('2015-12-01 12|2015-12-01 13|2015-12-01 14|2015-12-01 15',x[3])
##                if temp:
##                    c4+=1
##                temp=re.findall('2015-12-01 16|2015-12-01 17|2015-12-01 18|2015-12-01 19',x[3])
##                if temp:
##                    c5+=1
##                temp=re.findall('2015-12-01 20|2015-12-01 21|2015-12-01 22|2015-12-01 23',x[3])
##                if temp:
##                    c6+=1
##            if i.count('2015-12-02'):
##                x = ast.literal_eval(i)
##                temp=re.findall('2015-12-02 00|2015-12-02 01|2015-12-02 02|2015-12-02 03',x[3])
##                if temp:
##                    c7+=1
##                temp=re.findall('2015-12-02 04|2015-12-02 05|2015-12-02 06|2015-12-02 07',x[3])
##                if temp:
##                    c8+=1
##                temp=re.findall('2015-12-02 08|2015-12-02 09|2015-12-02 10|2015-12-02 11',x[3])
##                if temp:
##                    c9+=1
##                temp=re.findall('2015-12-02 12|2015-12-02 13|2015-12-02 14|2015-12-02 15',x[3])
##                if temp:
##                    c10+=1
##                temp=re.findall('2015-12-02 16|2015-12-02 17|2015-12-02 18|2015-12-02 19',x[3])
##                if temp:
##                    c11+=1
##                temp=re.findall('2015-12-02 20|2015-12-02 21|2015-12-02 22|2015-12-02 23',x[3])
##                if temp:
##                    c12+=1
##
##print(c1)
##print(c2)
##print(c3)
##print(c4)
##print(c5)
##print(c6)
##print(c7)
##print(c8)
##print(c9)
##print(c10)
##print(c11)
##print(c12)
##print("==============================================================")
##
##fig, ax=plt.subplots()
##index=np.arange(13)
##bar_width=0.15
##opacity=0.9
##
##belief0=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)
##y0=[1,2,3,4,5,6,7,8,9,10,11,12]
##
##
##content=codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
##regex = r"\w*chembarambakkam\w*"
##c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=0
##for i in content:
##    matches = re.finditer(regex,i)
##
##    for match in matches:
##        if match:
##            #print(i)
##            if i.count('2015-12-01'):
##                x = ast.literal_eval(i)
##                temp=re.findall('2015-12-01 00|2015-12-01 01|2015-12-01 02|2015-12-01 03',x[3])
##                if temp:
##                    c1+=1
##                temp=re.findall('2015-12-01 04|2015-12-01 05|2015-12-01 06|2015-12-01 07',x[3])
##                if temp:
##                    c2+=1
##                temp=re.findall('2015-12-01 08|2015-12-01 09|2015-12-01 10|2015-12-01 11',x[3])
##                if temp:
##                    c3+=1
##                temp=re.findall('2015-12-01 12|2015-12-01 13|2015-12-01 14|2015-12-01 15',x[3])
##                if temp:
##                    c4+=1
##                temp=re.findall('2015-12-01 16|2015-12-01 17|2015-12-01 18|2015-12-01 19',x[3])
##                if temp:
##                    c5+=1
##                temp=re.findall('2015-12-01 20|2015-12-01 21|2015-12-01 22|2015-12-01 23',x[3])
##                if temp:
##                    c6+=1
##            if i.count('2015-12-02'):
##                x = ast.literal_eval(i)
##                temp=re.findall('2015-12-02 00|2015-12-02 01|2015-12-02 02|2015-12-02 03',x[3])
##                if temp:
##                    c7+=1
##                temp=re.findall('2015-12-02 04|2015-12-02 05|2015-12-02 06|2015-12-02 07',x[3])
##                if temp:
##                    c8+=1
##                temp=re.findall('2015-12-02 08|2015-12-02 09|2015-12-02 10|2015-12-02 11',x[3])
##                if temp:
##                    c9+=1
##                temp=re.findall('2015-12-02 12|2015-12-02 13|2015-12-02 14|2015-12-02 15',x[3])
##                if temp:
##                    c10+=1
##                temp=re.findall('2015-12-02 16|2015-12-02 17|2015-12-02 18|2015-12-02 19',x[3])
##                if temp:
##                    c11+=1
##                temp=re.findall('2015-12-02 20|2015-12-02 21|2015-12-02 22|2015-12-02 23',x[3])
##                if temp:
##                    c12+=1
##
##print(c1)
##print(c2)
##print(c3)
##print(c4)
##print(c5)
##print(c6)
##print(c7)
##print(c8)
##print(c9)
##print(c10)
##print(c11)
##print(c12)
##print("==============================================================")
##
##fig, ax=plt.subplots()
##index=np.arange(13)
##bar_width=0.15
##opacity=0.9
##
##belief1=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)
##y1=[1,2,3,4,5,6,7,8,9,10,11,12]
##plt.plot(y,belief)
##plt.xlabel('Time in hrs')
##plt.ylabel('No. of tweets')
##plt.xticks(index+(6.6*bar_width),('0-3','4-7','8-11','12-15','16-19','20-23','0-3','4-7','8-11','12-15','16-19','20-23'))
##plt.plot(y,belief,'bo',linestyle='-')


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
print("==============================================================")


fig, ax=plt.subplots()
index=np.arange(13)
bar_width=0.15
opacity=0.9

belief2=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)
y2=[1,2,3,4,5,6,7,8,9,10,11,12]
##plt.plot(y,belief)
##plt.xlabel('Time in hrs')
##plt.ylabel('No. of tweets')
##plt.xticks(index+(6.6*bar_width),('0-3','4-7','8-11','12-15','16-19','20-23','0-3','4-7','8-11','12-15','16-19','20-23'))
##plt.plot(y,belief,'bo',linestyle='-')


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
print("==============================================================")

fig, ax=plt.subplots()
index=np.arange(13)
bar_width=0.15
opacity=0.9

belief3=(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12)
y3=[1,2,3,4,5,6,7,8,9,10,11,12]
#plt.plot(y0,belief0,y1,belief1,y2,belief2,y3,belief3)
plt.xlabel('Time in hrs')
plt.ylabel('No. of tweets')
plt.xticks(index+(6.6*bar_width),('0-3','4-7','8-11','12-15','16-19','20-23','0-3','4-7','8-11','12-15','16-19','20-23'))
plt.plot(y2,belief2,'bo',linestyle='-',label='Little girl lost')
plt.plot(y3,belief3,'yo',linestyle='-',label='Passport Damaged')
plt.legend()
plt.show()
