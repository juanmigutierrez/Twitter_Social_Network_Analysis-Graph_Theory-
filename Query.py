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
path3 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file3.txt"
path4 = r"C:\Users\Recup\OneDrive\Documentos\Proyecto_Graf\file4.txt"


file1 = open(path1, "wt")
#file2 = open(path2, "wt")
#file3 = open(path3, "wt")
#file4 = open(path4, "wt")


def noticias(query, f):
    k = 0
    for user in tw.Cursor(api.search, query).items():
        f.write(query+" "+user.user.screen_name+"\n")
        print(user.user.screen_name)
        k += 1
        if k== 1000 :
            break

noticias ("Venezuela", file1)