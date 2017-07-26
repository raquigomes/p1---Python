#Pratica 3
#1.1
def inteiro(num):
    p=0
    while p<=num-1:
        print(p)
        p=p+1

def inteiros(numero):
    h=0
    for h in range(numero):
        numero=h
        print(numero)
        h+=1

#1.2
def soma_inteiro(n):
    for i in range(n):
        n+=i
        i+=1
    print(n)

def soma(numb):
    j=1
    ssoma=0
    while j<=numb:
        ssoma+=j
        j+=1
    print(ssoma)

#2
def linha(l1,l2):
    r=' '    
    for c in range(2):
        r+=l1+4*l2
    r+=l1
    print(r)

def grelha():
    for i in range(2):
        linha('+',' -')
        for b in range(4):
              linha('|','  ')
    linha('+',' -')
grelha()

    
    
