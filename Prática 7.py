#Prática 7
#1
def soma_c(lista):
    r=[]
    for i in range (len (lista)):
        if i==0:
            r.append(lista[0])
        else:
            r.append(lista[i]+r[-1])
    return r


    
#2
def verifica_ordem(lista):
    if len(lista)==1:
        return True
    if lista[0]<=lista[1]:
        del(lista[0])
        return verifica_ordem(lista)
    else:
        return False

def verifica(l):
    if len(l)==1:
        return True
    elif l[0]<=l[1]:
        return True
    else:
        return False
#3
#3.1
def corta(lista):
    del(lista[0], lista[-1])
    return None

#3.2
def meio(lista):
    del(lista[0], lista[-1])
    return lista


#4
def e_anagrama(a,b):
    palavra1=list(a)
    palavra2=list(b)
    palavra1.sort()
    palavra2.sort()
    if palavra1 == palavra2:
       return True
    else:
        return False

def anagrama(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        palavra1=list(s1)
        palavra2=list(s2)
        palavra1.sort()
        palavra2.sort()
        if palavra1==palavra2:
            return True

#5
def conta_elementos(lista1, lista2):
    c=0
    for i in lista1:
        if i in lista2:
            c+=1
    if c>0:
        print(c, 'elementos em comum')
    else:
        print('Não possuem elementos em comum')
            

#6
def soma_colunas(matriz):
    lst=[]
    for i in matriz:
        lst+=i
        print(lst)
                
    




    
