#1.1 iterativa
def letras(s):
    if isinstance (s,str):
        i=0
        while i<len(s):
            print(s[i])
            i+=1
            
#1.1 recursiva
def letra(st):
    if len(st)==1:
        print(st)
    else:
        print(st[-1])
        letra(st[0:len(st)-1])
        


#1.2 iterativa
def escala(palavra):
    if isinstance(palavra,str):
        j=0
        while j<(len(palavra)):
            print(palavra[j:len(palavra)-1])
            j+=1

#12 recursiva
def escala_in(palav):
    if isinstance(palav,str):
        if len(palav)==0:
            print('Acabou')
        else:
            print(palav[0:len(palav)])
            escala_in(palav[0:len(palav)-1])


#2
def find(p,l,n):
    nr=int(n)
    while nr<len(p):
        if p[nr]==l:
            return nr
        nr+=1
    return -1

#5
def conta_palavras(*args):
    count=0
    for i in args:
        count+=1
    return count

def conta_palavra(s):
    final=0
    for i in s:
        string.whitespace(s)
        
    
    

