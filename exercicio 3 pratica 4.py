def portas_logicas():
    OR='OR'
    AND='AND'
    x=str(input("'AND' or 'OR': "))
    y=bool(input('1ºBooleano: '))
    z=bool(input('2ºBooleano: '))
    if z==True and x==OR or y==True and x==OR:
        print(True)
    elif z==True and y==True and x==AND:
        print('True')
    else:
        print('False')

portas_logicas()
    
