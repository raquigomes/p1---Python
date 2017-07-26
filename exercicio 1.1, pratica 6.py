def letras(n):
    if len(n)==1:
        print(n)
    else:
        print(n[-1])
        letras(n[:len(n)-1])
