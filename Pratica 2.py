#Pratica 2
#1
def multiplica(m,n):
    final=m*n
    print("A multiplicação de m por n é igual a %i" % final)


#2
def right_justify(string):
    result=(' '*(70-len(string))+string)
    print(result)


#3
def unidade(number):
    algarismo=int(number%10)
    print("O algarismo das dezenas é %i" % algarismo)

