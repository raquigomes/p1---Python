#1
def compara(x,y):
    if  x>y:
        return 1
    elif x==y:
        return 0
    elif x<y:
        return -1
    else:
        return None


#2
import math
def hipotenusa(cateto1,cateto2):
    return round((math.sqrt(cateto1**2+cateto2**2)),2)


#3
def ack(m,n):
    if isinstance(n, int) and isinstance(m,int):
        if m==0:
            return n+1
        elif m>0 and n==0:
            return ack(m-1,1)
        elif m>0 and n>0:
            return ack(m-1,ack(m,n-1))
        else:
            print('Valores tem que ser maiores que zero')
    else:
        print('Valores tem que ser inteiros')

#4
def b(z):
    prod=a(z,z)
    print(z,prod)
    return prod

def c(g,h,i):
    sum=g+h+i
    pw=b(sum)**2
    return pw

def a(o,p):
    o=o+1
    return 0*p
o=1
p=o+1

#5
def palavra1(palavrinha):
def palavra2(palavrinha):
def palavra3(palavrinha):
def palindromo(palavrinha):


#6
def mdc(n1, n2):
    if isinstance(n1,int) and isinstance(n2,int):
        r=max(n1,n2)
        t=min(n1,n2)
        if r%t==0:
            return n2
        else:
            return mdc(n2,(r%t))
    else:
        print('Valores tem que ser inteiros')
        
#7
#1)
def print_n(k,f):
    if f<=0:
        return
    print(k)
    print_n(k,f-1)
    
#2)
def print_nn(q,u):
    while u<=0:
        return print_nn(q,u-1)
    print(q)
