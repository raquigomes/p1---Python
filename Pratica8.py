#Pratica 8
#1
def histograma(s):
    d=dict()
    for c in s:
        if c in d:
            d[c]+=1
            d.get(c)
        else:
            d[c]=1
    return d

#2
def print_hist(h):
    n=list(h)
    n.sort()
    for c in n:
        print(c,h[c])

#3
def reverse_lookup(d,v):
    l=[]
    for c in d:
        if d[c]==v:
            l.append(c)
    return l
