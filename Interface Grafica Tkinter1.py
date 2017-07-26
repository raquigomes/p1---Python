#Primeiro Modo Grafica tkinter
#TOO MUCH
import tkinter
from tkinter import messagebox as tkMessageBox
import random


#Criacao do ambiente grafica do menu do jogo
window=tkinter.Tk() #Janela do tkinter
window.title("Ouri") #Nome da janela de jogo
window.geometry("700x400") #Tamanho da janela de jogo
#window.wm_iconbitmap('alien.ico')#importar um icone para pasta
btnsair=tkinter.Button(window,text="Sair do jogo")
lbljogo=tkinter.Label(window,text="Bem vindo ao Jogo do Ouri\n")
lblp1=tkinter.Label(window,text="\nInsira o Nome do Jogador 1\n")
entp1=tkinter.Entry(window)
lblp2=tkinter.Label(window,text="\nInsira o Nome do Jogador 2\n")
entp2=tkinter.Entry(window)
btnjogar=tkinter.Button(window,text="Novo Jogo")



lbljogo.pack()
btnsair.pack()
lblp1.pack()
entp1.pack()
lblp2.pack()
entp2.pack()
btnjogar.pack()
top.mainloop()


