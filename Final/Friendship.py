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
api = tw.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def analisis_di(G):
    betweenss = nx.betweenness_centrality(G, normalized= True, endpoints=False, k=10)
    page_rank = nx.pagerank(G)
    excentricidad = nx.edge_connectivity(G)
    periferia = nx.periphery(G)
    centro = nx.center(G)
    radio = nx.radius(G)
    cluster = nx.average_clustering(G)
    diametro = nx.diameter(G)
    #Cual es el menor numero de nodos necesarios para desconectar la red
    con_node = nx.node_connectivity(G)
    con_edge = nx.edge_connectivity(G)
    min_edge = nx.minimum_edge_cut(G)
    min_cut = nx.minimum_node_cut(G)
    print("Centralidad:",betweenss)
    print("                     -      ")
    print("Page_Rank:",page_rank)
    print("Periferia:",periferia)
    print("Excentricidad:",excentricidad)
    print("Centro:",centro)
    print("Nodo Conectividad:",con_node)
    print("Aristas_Conectividad:",con_edge )
    print("Aristas de Corte:",min_edge)
    print("Nodos de Corte:",min_cut)
    print("Radio:",radio)
    print("Cluster:",cluster)
    print("Diametro",diametro)
def analisis_multidi(G):
    betweenss = nx.betweenness_centrality(G, normalized= True, endpoints=False, k=10)
    print("Centralidad:",betweenss)


def followers(a,usuario):
    user = api.get_user(usuario)
    fol_cont = user.followers_count
    if (a>5 or user.followers_count==0 ):
        print("Usuario Anadido")
    else:
       if(fol_cont/100<5 and int(fol_cont/100 != 0 )):
            for user in tw.Cursor(api.followers, usuario).items(int(fol_cont/100)):
                archivo.write( usuario+" "+user.screen_name+'\n')
                nom = user.screen_name
                followers(a+1,nom)

###ACA VIENE CODIGO QUE BUSCA USUARIO Y SEGUIDORES 
screen_name ="miilano101"
user = api.get_user(screen_name)
fol_cont = user.followers_count
#print(user.followers_count)
followers(1,screen_name)

archivo.close() ###ABRIR ESTE CUANDO SE ABRA USUARIO

##GRAFOS###

G2 = nx.read_adjlist(path, nodetype=str,create_using=nx.DiGraph())

node_color = [G2.degree(v) for v in G2]
pos = nx.random_layout(G2)
#G2.add_edges_from([(0, 1),(0, 2), (0, 3)])
print(G2.edges())

nx.draw_networkx(G2,pos,node_color=node_color,alpha=0.7)
plt.savefig("Friendship.png")
plt.show()

###### ANALISIS #######
G1 = nx.read_adjlist(path, nodetype=str,create_using=nx.Graph())

print("Analisis Grafo")
analisis_di(G1)