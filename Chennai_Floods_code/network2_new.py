import pandas as pd
import codecs
import numpy as np
import networkx as nx
#from networkx.drawing.nx_agraph import graphviz_layout
import re
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

#data = pd.read_csv('edges.csv')
DG=nx.DiGraph()
data = codecs.open('Cluster3 Tweets.txt',"r",encoding="utf-8")
regex = r"\w*little girl\w*"
val_map={}
slist=[]
tlist=[]
olist=[]
#plt.figure(figsize=(10,10))
for i in data:
    d=i.split(',')
    time=d[3].replace("'","").strip().replace("\\r","").replace("\n","").replace("]","")
    matches = re.finditer(regex,d[2])
    for match in matches:
        if match:
            if time<='2015-12-05 23:59:59':
                #print(i)
                #sor=d[1]
                #tar=d[0]
                #print("sor",sor)
                #print("tar",tar)
                sor=d[1].replace('[','').replace("'",'').strip()
                tar=d[0].replace("'",'').replace(" ",'').replace('[','').strip()
                #print((sor,tar))
                if sor==tar:
                    #print(i)
                    #print((sor,tar,d[2]))
                    #print("olist sor",sor)
                    olist.append(sor)
                    DG.add_node(sor)
                    val_map.update({sor: 'y'})
                else:
                    #print(i)
                    #print("slist sor",sor)
                    #print("tlist",tar)
                    slist.append(sor)
                    tlist.append(tar)
                    DG.add_edge(sor,tar)
                    #if sor in val_map:
                        #print(val_map)
                    val_map.update({tar:'r',sor:'y'})

#print(len(set(slist)))
#print(len(set(tlist)))
#print(len(set(olist)))
from collections import Counter
print(Counter(val_map.values()))
#print(len(val_map.values()))
#print(sorted(DG.degree, key=lambda x: x[1], reverse=True))
values = [val_map.get(node, 0.25) for node in DG.nodes()]
pos = nx.spring_layout(DG,scale=2)
#degrees = [val for (node, val) in DG.degree()]
#print(DG.nodes())
#print(DG.edges())
#sel_edges = [(node, val) for (node, val) in DG.edges() if node=='Sibi_Sathyaraj' or val=='Sibi_Sathyaraj']
#print(sel_edges)
#sel_node = [val for (node, val) in sel_edges]
#sel_node.append('Sibi_Sathyaraj')
#print(sel_node)
#print(sorted(DG.degree, key=lambda x: x[1], reverse=True))
nx.draw(DG,pos,node_color=values)
#nx.draw(DG,pos=graphviz_layout(DG,prog='dot'),with_labels=True,nodelist=sel_node,edgelist=sel_edges,node_color=values)
#nx.draw(DG,pos=graphviz_layout(DG,prog='fdp'),node_color=values)

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Original Tweeter',
                          markerfacecolor='y', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Retweeter',
                          markerfacecolor='r', markersize=15)]
plt.legend(handles=legend_elements, loc='lower right')
plt.show()




   
