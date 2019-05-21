import tweepy as tw
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\Users.txt"
    
archivo = open (path, "wt")

consumer_key= 'b3xOQ7MqJNDFAcXwOx35JdbSX'
consumer_secret= 'VKQNJCJW05YEFgaA6nfdR4x2BqrvpDdA9s0xykQGGAxGkCT9Bb'
access_token= '780626992550989824-eDyB0LaTPTYig1JDK5X0t4SQPD7lw6W'
access_token_secret= 'rOBoLqzODfnRoFn8VbZrJCf7gVfrShaRYZtM3rvOUgtiG'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

path1 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file1.txt"
path2 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file2.txt"
path4 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\Union.txt"


file1 = open(path1, "wt")
file2 = open(path2, "wt")


def noticias(query, f):
    k = 0
    for user in tw.Cursor(api.search, query).items():
        f.write(query+" "+user.user.screen_name+"\n")
        print(user.user.screen_name)
        k += 1
        if k== 1000 :
            break

Palabra1= "Google"
Palabra2 = "Huawei"
noticias (Palabra1, file1)
noticias (Palabra2, file2)


def intersect(lista_comun,f,query1,query2):
    for user in lista_comun:
        f.write(query1+" "+user+"\n")
        f.write(query2+" "+user+"\n")


file1.close()
file2.close()

G1 = nx.read_adjlist(path1, nodetype=str,create_using=nx.Graph())
G2 = nx.read_adjlist(path2, nodetype=str,create_using=nx.Graph())

#Graficos Noticias Uniendo los dos

try:
    G3 = nx.compose(G1,G2)
    lista_comun = list(nx.common_neighbors(G3,Palabra1,Palabra2))
    file4 = open(path4, "wt")
    intersect(lista_comun,file4,Palabra1,Palabra2)
    file4.close()


    G4 = nx.read_adjlist(path4, nodetype=str,create_using=nx.Graph())
    node_color = [G4.degree(v) for v in G4]
    pos = nx.circular_layout(G4)

    nx.draw_networkx(G4, pos, alpha=0.7,node_color=node_color,cmap='Blues')
    print()
    plt.axis('off')
    plt.savefig("Relationship.png")
    plt.show()

    aristas = G4.number_of_edges()
    estadistico = (aristas/2000)*100
    print("Estadistico:%",estadistico)

except:
    print("Los Temas no poseen relación alguna")


