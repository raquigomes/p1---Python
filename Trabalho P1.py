'''Funcao main que cria as variaveis base para a inicializacao do
jogo: lista de listas das casas de cada jogador e os depositos de
cada jogador inicializados a zero'''
def main():
    jogo = criartabuleiro()
    #tabuleiro do jogador 1
    tab1 = jogo[0][0]
    #tabuleiro do jogador 2
    tab2 = jogo[0][1]
    #deposito do jogador 1
    j1 = jogo[1]
    #deposito do jogador 2
    j2 = jogo[2]
    #chama a funcao jogadores para pedir o nome dos dois jogadores
    tabjog = jogadores(tab1, tab2, j1, j2)
    #Enquanto o jogo nao acabar executa o ciclo while
    fimdejogo = False
    while fimdejogo == False:
        #Para as  jogadas do jogador1
        casaJogada = pedeJogada(tab1, j1, tab2, tabjog[0])
        jogadaOk1 = jogada(casaJogada, tab1, j1, tab2)
        fimdejogo = jogadaOk1[0]
        tab1 = jogadaOk1[1]
        j1 = jogadaOk1[2]
        tab2 = jogadaOk1[3]
        imprimeTabuleiro(tab1, tab2, tabjog[0], j1, tabjog[1], j2)
        
        #Para as jogadas do jogador2
        casaJogada = pedeJogada(tab2, j2, tab1, tabjog[1])
        jogadaOk2 = jogada(casaJogada, tab2, j2, tab1)
        fimdejogo = jogadaOk2[0]
        tab2 = jogadaOk2[1]
        j2 = jogadaOk2[2]
        tab1 = jogadaOk2[3]
        imprimeTabuleiro(tab1, tab2, tabjog[0], j1, tabjog[1], j2)

    finalizarJogo(j1, j2, tabjog[0], tabjog[1])

        

'''Ficheiro main dado pelo professor: constituido pelas funcoes menu que
imprime as varias opcoes de jogo para o utilizador escolher o modo em que quer jogar
'''
def menu():
    print('0 - Sair')
    print('1 - Humano vs Humano: modo texto')
    print('2 - Humano vs Humano: modo grafico')
    print('3 - Humano vs Computador')
    #Pede o input da opcao que o utilizador quer jogar
    b = input('Escolha uma opção de 0 a 3: \n')
    if b == '0':
        #Escolhida a opcao zero o jogo termina
        print('O jogo Terminou')
        return None # evita que volte a escrever o menu com os print 0 a 3
    if b == '1':
        #escolhida a opcao um o jogo prossegue em modo texto para a funcao incicio
        inicio(b)
    #if b == '2':
        #g.mainloop(b)
    #if b == '3':
        #ComputerRules(c)     
    else:
        #Se nao for introduzido um valor valido
        print('Opcao nao existe, escolha opcao de 0 a 3')
        menu()



'''Funcao inicio que faz print dos objectivos principais do jogo e identifica
por quem o trabalho foi realizado e que consoante as opcoes de escolha corre
o programa de jogo pedido'''
def inicio(opcao):
    print('##############################  Jogo Ouri  ##############################')
    print('#                 Recolher mais pecas que o adversario                  #')
    print('#              Ganha o jogador que tiver mais de 25 peças               #')
    print('#                   Todas as pecas tem o mesmo valor                    #')
    print('#    Joao Marques - 31514  Raquel Gomes - 31523  João Vieira - 32445    #')
    print('#########################################################################')
    if opcao == '0':
        #se for escolhida a opcao zero o jogo termina e sai
        print('O jogo terminou')
        menu()
    elif opcao == '1':
        #se for escolhida a opcao um: o jogo prossegue atraves da funcao main
        main()
    #elif opcao == '2':
        #main()
    #elif opcao == '3':
        #return



'''Funcao criartabuleiro que cria o tabuleiro geral do jogo e os depositos
dos dois jogadores inicializados a zero'''
def criartabuleiro():
    #lista das casas de cada jogador
    tabuleiro = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    #deposito do jogador 1
    j1 = 0
    #deposito do jogador 2
    j2 = 0
    #retorna lista com o tabuleiro e os dois depositos
    return [tabuleiro, j1, j2]



'''Funcao imprimeTabuleiro que recebe como argumentos o tabuleiro do
jogador 1 e do jogador 2,o nome de cada jogador e os respectivos depositos
e faz o print do desenho do tabuleiro'''
def imprimeTabuleiro(tabuleiro1, tabuleiro2, jogador1, j1, jogador2, j2):
    #imprime o nome e deposito do jogador 1
    print('          ', jogador2, j2, '          ')
    #imprime o tabuleiro com as listas dos dois jogadores
    print('  ', tabuleiro2[::-1], '\n', ' ', tabuleiro1)
    #imprime o nome e deposito do jogador 2
    print('          ', jogador1, j1, '          ')



'''Funcao jogadores que recebe como argumentos o tabuleiro
o deposito do jogador 1 e o tabuleiro do jogador 2 e os
depositos dos dois jogadores e pede o input do nome de cada
jogador e se os nomes forem iguais nao aceita e volta a pedir
os inputs de novo'''
def jogadores(tabuleiro1, tabuleiro2, j1, j2):
    #input do nome do jogador 1
    jogador1 = input('Introduza nome jogador 1: \n')
    #input do  nome do jogador 2
    jogador2 = input('Introduza nome jogador 2: \n')
    if jogador1 == jogador2:
        #se os nomes forem iguais pede novos nomes
        print('Introduza nomes diferentes')
        #input do nome dos jogadores novamente
        jogadores(tabuleiro1, tabuleiro2, j1, j2)
    else:
        #imprime o tabuleiro base de jogo com os nomes e depositos dos jogadores
        imprimeTabuleiro(tabuleiro1, tabuleiro2, jogador1, j1, jogador2, j2)
    #retorna uma lista com os dois jogadores e os respetivos depositos
    return [jogador1, jogador2, j1, j2] #tabjog




'''Funcao escolhaJogada que verifica se a casa que o jogador escolheu
tem pecas e se pode jogar em casas com uma peca se as restantes
tiverem uma ou menos pecas'''
def escolhaJogada(casaEscolhida, casasJogador):
    #Verifica se a casa escolhida tem mais do que uma peca
    if casasJogador[casaEscolhida] > 1:
        return True
    #se a casa tem 1 peca e o maximo possivel nas outras do mesmo jogador e 1
    elif casasJogador[casaEscolhida] == 1 and max(casasJogador) == 1:
        return True
    #outros casos retorna sempre False
    else:
        return False



'''Funcao pedeJogada que recebe como argumentos o total e as casas
do jogador e do seu adversario e pede uma casa para jogar e
verifica se inseriu uma casa valida'''
def pedeJogada(tabuleiroJogador, totalJogador, tabuleiroAdversario, nomeJogador):
    print("\nVez do jogador", nomeJogador)
    #Excepcao para verificar se o input da casa e valido
    while True:
        try:
            #Pede um inteiro da casa onde quer jogar de 1 a 6
            jogada=int(input('De 1 a 6 escolha o numero da casa onde quer jogar: '))
        except ValueError:
            #Se nao for um inteiro de 1 a 6 gera a excepcao
            #Volta a pedir que insira o valor de novo
            print('Escolha uma casa com um inteiro válido entre 1 e 6!')
        else:
            #Verifica se o jogador jogou anteriormente na casa escolhida
            if 0<jogada<7 and escolhaJogada(jogada -1, tabuleiroJogador) == True:
                break         
            else:
                print('Jogada invalida')
    print('Vai jogar na casa ',jogada,'. Todas as peças serão removidas dessa casa')
    return (jogada -1)
            



'''Funcao jogada que recebe como argumentos a casa da jogada, o tabuleiro do
jogador que esta a jogar, o total do deposito desse jogador e o tabuleiro do
adversario, e que apos realizar a jogada verifica se o deposito ja tem mais
de 24 pecas ou nao, para verificar se termina o jogo ou nao'''
def jogada(casaJogada, tabuleiroJogador, totalJogador, tabuleiroAdversario):
    #faz chamada da funcao realizar jogada e guarda na variavel
    actjog = realizarJogada(casaJogada,tabuleiroJogador,totalJogador,tabuleiroAdversario)
    tabuleiroJogador = actjog[0]
    totalJogador = actjog[1]
    tabuleiroAdversario = actjog[2]
    #verifica se o total do deposito tem mais de 24 pecas
    if totalJogador > 24:
        #se sim retorna True e acaba o jogo
        return [True, tabuleiroJogador, totalJogador, tabuleiroAdversario]
    else:
        #Se nao continua a jogar
        return [False, tabuleiroJogador, totalJogador, tabuleiroAdversario]





'''Funcao retirarPecas que recebe como argumentos a casa onde fica a ultima peca,
o tabuleiro do adversario e o total do deposito do jogador e verifica se as casas
onde ficaram as ultimas pecas da jogada tem 2 ou 3 pecas, e se assim for serao
retiradas e guardadas no deposito do jogador'''
def retirarPecas(ultimaCasa, tabuleiroAdversario, totalJogador):
    for c in range(ultimaCasa + 1):
        #Verifica se as ultimas casas tem 2 ou 3 pecas
        if tabuleiroAdversario[ultimaCasa-c]==2 or tabuleiroAdversario[ultimaCasa-c]==3:
            #Adiciona essas pecas ao deposito do jogador
            totalJogador += tabuleiroAdversario[ultimaCasa-c]
            #Mete a zero as casas das pecas que retirou
            tabuleiroAdversario[ultimaCasa-c]=0
        else:
            #outros casos faz o break do ciclo
            break
        #retorna a lista com o total do deposito do jogador e o tabuleiro
    return [totalJogador, tabuleiroAdversario]
    
    
    
'''Funcao realizarJogada que recebe como argumentos a casa onde o jogador quer
realizar a jogada, o tabuleiro do jogador, o deposito do jogador e o tabuleiro
do aversario, e conta o numero de pecas que tinha na casa onde vai ser feita a
jogada e as espalha pelas casas a seguir; Verifica tambem se pode ou nao
recolher as pecas se na casa onde parou estiverem 2 ou 3 pecas'''
def realizarJogada(casaJogada, tabuleiroJogador, totalJogador, tabuleiroAdversario):
    #tira as pecas da casa que o jogador quer jogar
    #guarda-as na variavel guardarPedras
    guardarPedras = tabuleiroJogador[casaJogada]
    #Mete a 0 a casa onde foi efectuada a jogada
    tabuleiroJogador[casaJogada] = 0
    #inicializa tres contadores a 0
    #variavel i para percorrer as casas do jogador actual (1 vez)
    #variavel z para percorrer as casas do jogador adversario
    #variavel t para percorrer as casas do jogador actual (x vez)
    i = z = t = 0
    while i < guardarPedras:
        if casaJogada + 1 + i < 6:
            #Vai largando as pecas nas casas do jogador actual
            tabuleiroJogador[casaJogada + 1 + i] += 1
        elif z < 6:
            #Vai largando as pecas nas casas do jogador adversario
            tabuleiroAdversario[z] +=1
            z += 1
        elif t == casaJogada:
            #Salta a casa inicial da jogada actual
            t += 1
            guardarPedras +=1
        elif t < 6:
            #vai largando as pecas nas casas do jogador actual
            tabuleiroJogador[t] +=1
            t += 1
        else:
            z = t = 0
        i += 1

    ultimaCasa = z - 1 # valor residual devido ao valor de z na funçao realizar jogada
    #depois do valor i terminar o valor z adiciona +1 no incremento
    if z!=0 and t == 0 and 1 < tabuleiroAdversario[ultimaCasa] < 4:
        #verifica se ficaram 2 ou 3 pecas na ultima casa da jogada
        totalRetiradas = retirarPecas(ultimaCasa, tabuleiroAdversario, totalJogador)
    else:
        return [tabuleiroJogador, totalJogador, tabuleiroAdversario]
    #totalRetiradas[0]->totalJogador, totalRetiradas[1]->tabuleiroAdversario
    return [tabuleiroJogador, totalRetiradas[0], totalRetiradas[1]]


'''Funcao finalizarJogo que recebe como argumentos o total dos depositos
dos dois jogadores e os nomes dos respectivos jogadores e finaliza o jogo
e apresenta o vencedor ou uma mensagem de empate caso ocorra'''
def finalizarJogo(total1, total2, nome1, nome2):
    #Se o total do jogador 1 for maior que o total do jogador 2
    if total1 > total2:
        print('O Jogador', nome1, 'venceu!!')
    #Se o total do jogador 2 for maior que o total do jogador 1
    elif total2 > total1:
        print('O Jogador', nome2, 'venceu!!')
    else:
        print('Ocorreu um empate :|')
        
        


'''
#######PARTE GRAFICA########


import tkinter
from tkinter import *
from swampy import *
from swampy.Gui import *
g=Gui()
g.title('Ouri')


def sairdojogo():
    g.la(text='Você abandonou o jogo')
    
button=g.bu(text='0 - Sair do Jogo', command=sairdojogo)
button=g.bu(text='1 - Humano vs Humano: modo texto', command=inicio(1))
button=g.bu(text='2 - Humano vs Humano: modo grafico')
button=g.bu(text='3 - Humano vs Computador')
canvas = g.ca(width=1200, height=600)
canvas.config(bg='white')


#Funcao rectaP1 que desenha o rectangulo do deposito do jogador 1 com
#recurso ao canvas.rectangle
def rectaP1(g):
    item = canvas.rectangle([[150,60],[-500,100]],fill='white', outline='black', width=2)


#Funcao circP1 que desenha os circulos (casas do jogador 1) atraves de um ciclo
#for para os 6 circulos(6 casas) com recurso ao canvas.circle
def circP1(g):
    j=-450
    for i in range (0, 6):
        item = canvas.circle([j,0],50,fill='white', outline='black',width = 2)
        j+=100+10


#Funcao circP2 que desenha os circulos (casas do jogador 2) atraves de um ciclo
#for que desenha os 6 circulos (6 casas) com recurso ao canvas.circle
def circP2(g):      
    k=-450
    for h in range(0, 6):
        item = canvas.circle([k,-110],50,fill='white', outline='black', width = 2)
        k+=100+10


#funcao rectaP2 que desenha o rectangulo (deposito do jogador 2) com recurso ao
#canvas.rectangle
def rectaP2(g):
    item = canvas.rectangle([[150,-170],[-500,-210]],fill='white', outline='black', width=2)


print(rectaP1(canvas))
print(circP1(canvas))
print(circP2(canvas))
print(rectaP2(canvas))

g.mainloop()
'''

menu()
