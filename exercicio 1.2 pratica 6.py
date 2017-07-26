def escala_in(n):
    if len(n)==0:
        print('END')
    else:
        print(n[0:len(n)])
        escala_in(n[0:(len(n))-1])
