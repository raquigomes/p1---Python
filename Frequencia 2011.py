#1-Calcular area da superficie de uma esfera
import math
def area(raio):
    a=4*math.pi*raio**2
    print("O valor da área com o raio dado é %i" %a)


#2-Escrever uma string de modo a que fique ao centro de uma linha de 80 caracteres
def centrar(palavra):
        print(' '*(80-len(palavra))+palavra)


#3-Produto dos inteiros de 1 a n
'''?def produto(n):
    for m in range(n):
        n=n*m
        m+=1
    print(n)'''

#4-Verificar se se pode formama um triângulo
def e_triangulo(l1,l2,l3):
    if l1>0 and l2>0 and l3>0:
        if l1>l2+l3 or l2>l3+l1 or l3>l1+l2:
            print("É possivel formar um triângulo")
        else:
            print("Não é possivel formar um triangulo com os valores inseridos")

#5
        
