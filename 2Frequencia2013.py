#2a Frequencia 2013
#1a)
#Não está a funcionar corretamente
def conjunto(lista):
    c=0
    j=len(lista)-1
    for c in lista:
        if c<j:
            return False
        c+=1
        j-=1
        return True
        

#1b)
#A funcionar corretamente
def intersecao(conjunto1,conjunto2):
    count=[]
    for i in conjunto1:
        for j in conjunto2:
            if i==j:
                count.append(j)
        return count

#2a)
"""
Duas estruturas de Dados: Dicionários e Tuplos
"""

#2b)
def codificacao(dicionario):
    d={'A':'Alfa'}
    
#3
#A funcionar corretamente
def lista(tuplo):
    l=[]
    for i in tuplo:
        l.append(i)
    return l

#4
#Não está a funcionar corretamente
def binario(tuplobin):
    listabinaria=list(tuplobin)
    soma=0
    for x in listabinaria:
        if x!=0 and x!=1:
            print ('Não é um numero binario')
        else:
            soma=listabinaria[x]*2**listabinaria[x]
        return soma

#5a)
def campo_minado():
    f=open()
    f.writeline()

