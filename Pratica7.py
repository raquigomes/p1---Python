#1-soma de elementos da lista
def soma_c(num):
    lista=[]
    for i in range(len(num)):
        if i==0:
            lista.append(num[0])
        else:
            lista.append(num[i]+lista[-1])
    return lista

#2-Verificar se os elementos da lsita estão por ordem
