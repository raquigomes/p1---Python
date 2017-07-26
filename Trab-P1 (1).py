import random
'''def Ouri():
    x = input('0- Sair \n1- Humano vs Humano \n2- Humano vs Computador\n')
    if x == '0':
        print('O jogo terminou')
        #Termina o jogo e volta a mostrar o menu Ouri outra vez
        Ouri()
    elif x == '1':
        #chamada da funcao criarJogo e guarda na variavel inicio
        inicio = main()
        #chamada da funcao imprimeTabuleiro com argumentos a variavel inicio
        imprimeTabuleiro(inicio[2], inicio[3], inicio[4], inicio[5])
        #chamada da funcao play com argumentos a variavel inicio
        play(inicio[2], inicio[3], inicio[4], inicio[5], inicio[0], inicio[1])
    elif x == '2':
        #chamada da funcao criarJogo e guarda na variavel inicio
        inicio=main()
        #chamada a funcao imprimeTabuleiro com argumentos a variavel inicio
        imprimeTabuleiro(inicio[2], inicio[3], inicio[4], inicio[5])
    else:
        print('Introduza um valor valido: 0, 1 ou 2')
        return Ouri()

'''Funcao criarJogo para introduzir os inputs dos nomes dos jogadores
e para criar o tabuleiro com as casas dos jogadores 1 e 2 e os seus
respetivos depósitos'''
def main():
    print('Bem vindo ao jogo do Ouri')
    print('\n')
    #Input do nome do jogador 1 
    Player1 = (str(input('Introduza o nome do jogador 1: ')))
    print ('\n')
    #Input do nome do jogador 2
    Player2 = (str(input('Introduza o nome do jogador 2: ')))
    print('\n')
    print( Player1, 'vs' , Player2)
    print('\n')
    #Total do deposito do jogador 1
    deposito1=0
    #Total do deposito do jogador 2
    deposito2=0
    l=[[4,4,4,4,4,4], [4,4,4,4,4,4]]
    #Retorna lista com os jogadores, os depositos e o tabuleiro
    return [Player1, Player2, deposito1, deposito2, l[0], l[1]]


'''Funcao imprimeTabuleiro que recebe como argumentos o depósito do jogador 1
e o depósito do jogador 2 e a lista de casas do jogador 1 e do jogador 2'''    
def imprimeTabuleiro(deposito1, deposito2, casas1, casas2):
    print ('\n')
    #Percorrer as casas do jogador 2 e inverte-la
    for e in reversed(casas2):
        print('       ', e, end='')
    print('\n')
    #Imprime a linha do meio do tabuleiro onde aparecem os totais dos depositos dos dois jogadores
    print('P2','(',deposito2,')', ' '*45, '(',deposito1,')','P1', '\n')
    
    #Percorrer as casas do jogador 1 e imprimi-las
    for e in casas1:
        print('       ', e, end='')
    print('\n')


'''Funcao jogadaEscolhidaque recebe como argumentos a casa escolhida para jogar
e .. para verificar se o jogar pode efectuar a jogada nessa casa ou nao'''
def jogadaEscolhida(casaEscolha, casasJogador):
    #Verifica se a casa escolhida tem pecas
    if casasJogador[casaEscolha] > 1:
        return True
    #Verifica se a casa tem uma peca ou a casa so tem um numero
    elif casasJogador[casaEscolha] == 1 and max(casaEscolha) == 1:
        return True
    #outros casos retorna sempre False
    else:
        return False
    

'''Funcao pedeJogada que recebe como argumentos o total e as casas
do jogador e do seu adversario e pede uma casa para jogar e
verifica se inseriu uma casa valida'''
def pedeJogada(total, casasJogador, casasAdversario):
    #Excepcao para verificar se o input da casa e valido
    while True:
        try:
            #Pede um inteiro da casa onde quer jogar de 1 a 6
            jogadainput=int(input('Escolha uma casa de (1 a 6): '))
        except ValueError:
            #Se nao for um inteiro de 1 a 6 gera a excepcao
            #Volta a pedir que insira o valor de novo
            print('Insira um valor inteiro entre 1 e 6!')
        else:
            if 0<jogadainput<7 and jogadaEscolhida(jogadainput-1,casasJogador)==True:
                break
            else:
                print('Jogada invalida')
    return (jogadainput -1)
'''

#ATE AQUI
def jogada(totaljog, totalopon, zonajog, zonaopon, nomeJogador):
    print('Jogada do', nomeJogador)
    escolhaValida = pedeJogada(totaljog, zonajog, zonaopon)
    novaJogada = realizarJogada(totaljog, zonajog, zonaopon, escolhaValida)
    return [novaJogada[0], totalopon, novaJogada[1], novaJogada[2], novaJogada[3]]



def realizarJogada(total, casasJogador, casasAdversario, escolhaValida):
    pedras = casasJogador[escolhaValida]
    casasJogador[escolhaValida] = 0
    i = 0
    z = 0
    t = 0
    while (i < pedras): #usei o while para saltar a casa escolhida!
        if escolhaValida + 1 + i < 6 :
            casasJogador[escolhaValida + 1 + i] += 1
        elif z < 6 :
            casasAdversario[z] += 1
            z += 1
        elif t == escolhaValida:
            t += 1
            pedras += 1
        elif t < 6:
            casasJogador[t] += 1
            t += 1
        else:
            z = 0
            t = 0
        i += 1

    ultimaCasa = z - 1
    if z != 0 and t == 0 and 1 < casasAdversario[ultimaCasa] < 4:
        for c in range(z):
            if casasAdversario[ultimaCasa - c] == 2 or casasAdversario[ultimaCasa - c] == 3:
                total += casasAdversario[ultimaCasa - c]
                casasAdversario[ultimaCasa-c] = 0
                
            else:
                break
    if total > 24:
        fimJogo = True
    else:
        fimJogo = False
    
    return [total, casasJogador, casasAdversario, fimJogo]


    
def play(deposito1, deposito2, zona1, zona2, nomeJogador1, nomeJogador2):
    fimdeJogo = False
    while fimdeJogo == False:
        j1 = jogada(deposito1, deposito2, zona1, zona2, nomeJogador1)
        total1 = j1[0]
        zona1 = j1[2]
        zona2 = j1[3]
        fimdeJogo = j1[4]
        imprimeTabuleiro(deposito1, deposito2, zona1, zona2)
        
        j2 = jogada(total2, total1, zona2, zona1, nomeJogador2)
        total2 = j2[0]
        zona1 = j2[3]
        zona2 = j2[2]
        fimdeJogo = j2[4]
        imprimeTabuleiro(deposito1, deposito2, zona1, zona2) 
