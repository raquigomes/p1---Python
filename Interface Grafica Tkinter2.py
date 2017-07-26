import tkinter
from tkinter import *
from swampy import *
from swampy.Gui import *
#from CodigoDoIvo.py import *
g=Gui()
g.title('Ouri')


def sairdojogo():
    g.la(text='Você abandonou o jogo')
    
button=g.bu(text='0 - Sair do Jogo', command=sairdojogo)
button=g.bu(text='1 - Humano vs Humano: modo texto')
button=g.bu(text='2 - Humano vs Humano: modo grafico')
button=g.bu(text='3 - Humano vs Computador')
canvas = g.ca(width=1400, height =800)
canvas.config(bg='white')


#canvas.offset(0,0)
canvas.config(scrollregion=canvas.bbox(ALL))
x = canvas.canvasx(0)
y = canvas.canvasy(0)
canvas.find_closest(x, y)

def callback(ca):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print (canvas.find_closest(x, y))


def rectaP1(g):
    item = canvas.rectangle([[150,60],[-500,100]],fill='white', outline='black', width=2)
    
def circP1(g):
    j=-450
    for i in range (0, 6):
        item = canvas.circle([j,0],50,fill='white', outline='black',width = 2)
        j+=100+10
        
def circP2(g):      
    k=-450
    for h in range(0, 6):
        item = canvas.circle([k,-110],50,fill='white', outline='black', width = 2)
        k+=100+10
        
def rectaP2(g):
        
    item = canvas.rectangle([[150,-170],[-500,-210]],fill='white', outline='black', width=2)


print(rectaP1(canvas))

print(circP1(canvas))
print(circP2(canvas))
print(rectaP2(canvas))

g.mainloop()

# http://effbot.org/tkinterbook/canvas.htm#coordinate-systems
# http://www.brpreiss.com/books/opus7/
