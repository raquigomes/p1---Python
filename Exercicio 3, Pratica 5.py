def ack(m,n):
    if isinstance(m,int) and isinstance(n,int):
        if m>=0 and n>=0:
            if m==0:
                return n+1
            elif m>0 and n==0:
                return ack(m-1,1)
            else:
                return ack(m-1,ack(m,n-1))
            
        
    
