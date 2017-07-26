#Pratica4
#1
def numero_par(n):
    if n%2==0:
        return True
    else:
        return False


#2
def um_algarismo(u):
    l=len(str(u))
    if l==1:
        return True
    else:
        return False


#3
def portas_logicas(s,b1,b2):
    if s=='and':
        if b1==True and b2==True:
            return True
        else:
            return False
    elif s=='or':
        if b1==False and b2==False:
            return False
        else:
            return True
    else:
        return None
    
#4
def numero_meio(m1,m2,m3):
    if max(m1,m2,m3)==m1:
        return m1
    elif max(m1,m2,m3)==m2:
        return m2
    elif max(m1,m2,m3)==m3:
        return m3
    else:
        return None

#5
def triangulo(t1,t2,t3):
    if t1==0 or t2==0 or t3==0:
        print('Nao é um triangulo')
    elif t1+t2>t3 and t1+t3>t2 and t2+t3>t1:
        if t1==t2==t3:
            print('Os valores inseridos formam um triangulo equilatero')
        elif t1==t2 or t1==t3 or t2==t3:
            print('Os valores formam um triangulo isosceles')
        elif t1!=t2!=t3:
            print('Os valores inseridos formam um triangulo escaleno')
        else:
            print('Não é um triangulo')
    else:
        print('Não é um triangulo')

#6
def ano_bissexto(ano):
    if ano%4==0 and ano%100!=0:
        return True
    elif ano%4==0 and ano%400==0 and ano%100==0:
        return True
    else:
        return False

def data_valida(d,m,a):
    if d==29 and m==2 and ano_bissexto(a):
        print('Data Valida')
    else:
        print('Data Invalida')

#7
#a)
def factorial_rec(h):
    if not isinstance (h, int):
        print('Factorial só funciona com números inteiros')
    elif h<0:
        print('Factorial so esta definido para valores maiores ou iguais a 0')
    elif h==0:
        return 1
    else:
        return h*factorial_rec(h-1)
            
    
