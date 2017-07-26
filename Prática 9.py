#Pratica 9
#1
def sort_by_length(words):
    t=[]
    for word in words:
        t.append((len(word),word))
        
    t.sort(reverse=True)
    
    res=[]
    for length,word in t:
        res.append(word)
    return res

import random
#1Outra
def sortbylength(words):
    d = dict()
    for word in words:
        d[len(word)] = d.get(len(word),[]) + [word]

    lista=list(d.keys())
    lista.sort(reverse=True)
    
    for value in lista:
        valores=d[value]
        random.shuffle(valores)
        for valor in valores:
            print (valor)
    return None
