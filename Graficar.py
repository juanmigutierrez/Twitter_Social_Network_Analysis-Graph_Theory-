import tweepy as tw
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\Users.txt"
path2 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file1.txt"
path3 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file2.txt"
path4 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\Union.txt"

def intersect(lista_comun,f,query1,query2):
    for user in lista_comun:
        f.write(query1+" "+user+"\n")
        f.write(query2+" "+user+"\n")


"""p = nx.read_adjlist(path2, nodetype=str,create_using=nx.MultiDiGraph())
pos = nx.random_layout(p)
color_map = []
choose = [1,3]
for node in p:
    if int(node) in choose:
        print(int(node))

        color_map.append('blue')
    else :
        color_map.append('red')
   
nx.draw(p,node_color = color_map,with_labels = True)
#nx.draw_networkx(p, pos, node_color = 'r')

G2 = nx.read_adjlist(path, nodetype=str,create_using=nx.MultiDiGraph())
pos = nx.random_layout(G2)
nx.draw_networkx(G2, pos)"""

#Graficos Noticias Uniendo los dos
G1 = nx.read_adjlist(path2, nodetype=str,create_using=nx.Graph())
G2 = nx.read_adjlist(path3, nodetype=str,create_using=nx.Graph())
G3 = nx.compose(G1,G2)

#nx.draw_networkx(G3,pos,alpha=0.1, with_labels=False)
#print(nx.weakly_connected_components(G3))


## GRAFICOS GRAFO GRANDE ####
"""
pos = nx.random_layout(G3)
node_color = [G3.degree(v) for v in G3]
nx.draw_networkx(G3, pos, 
                 node_color=node_color, alpha=0.01, with_labels=False)

plt.axis('off')
plt.tight_layout()
plt.show()
"""
lista_comun = list(nx.common_neighbors(G3,'Venezuela','Maduro'))

##### CREANDO EL OTRO GRAFO INTERSECCION########

file4 = open(path4, "wt")

intersect(lista_comun,file4,"Venezuela","Maduro")
file4.close()


G4 = nx.read_adjlist(path4, nodetype=str,create_using=nx.Graph())
node_color = [G4.degree(v) for v in G4]
pos = nx.circular_layout(G4)

nx.draw_networkx(G4, pos, alpha=0.7,node_color=node_color,cmap='Blues')
print()
plt.axis('off')
plt.show()
