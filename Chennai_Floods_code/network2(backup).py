import pandas as pd
import codecs
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import re
import matplotlib.pyplot as plt

#data = pd.read_csv('edges.csv')
DG=nx.DiGraph()
data = codecs.open('Cluster2 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*crocodile\w*"
val_map={}
slist=[]
tlist=[]
olist=[]

#plt.figure(figsize=(10,10))
for i in data:
    d=i.split(',')
    matches = re.finditer(regex,d[2])
    for match in matches:
        if match:
            #print(i)
            #sor=d[1]
            #tar=d[0]
            #print("sor",sor)
            #print("tar",tar)
            sor=d[1].replace('[','').replace("'",'').strip()
            tar=d[0].replace("'",'').replace(" ",'').replace('[','').strip()
            #print((sor,tar))
            if sor==tar:
                #print((sor,tar,d[2]))
                olist.append(sor)
                DG.add_node(sor)
                val_map.update({sor: 'y'})
            else:
                slist.append(sor)
                tlist.append(tar)
                DG.add_edge(sor,tar)
                val_map.update({tar: 'r',sor:'b'})

print(len(set(slist)))
print(len(set(tlist)))
print(len(set(olist)))
values = [val_map.get(node, 0.25) for node in DG.nodes()]
pos = nx.spring_layout(DG,scale=2)
degrees = [val for (node, val) in DG.degree()]
#print(DG.degree())
#print(sorted(DG.degree, key=lambda x: x[1], reverse=True))
#nx.draw(DG,pos,with_labels=True,font_size=15,node_color=values)
nx.draw(DG,pos=graphviz_layout(DG),node_color=values)
plt.show()




##for i in data.iterrows():
##    s=i[1]['Source']
##    t=i[1]['Target']
##    for j in datan.iterrows():
##        if s==j[1]['Id']:
##            i[1]['Source']=j[1]['Label']
##        if t==j[1]['Id']:
##            i[1]['Target']=j[1]['Label']
##
##    print(i)
##
##FG = nx.from_pandas_edgelist(data, source='Source', target='Target', edge_attr=True,)
##print("Load Done")
###nx.draw_networkx(FG, with_labels=True)
##nx.write_graphml(FG,"Tweet.graphml")       
