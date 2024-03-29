w = [5,7,10,12,15,18,20]
m = 35
x = [0,0,0,0,0,0,0]

def SumofSubset(s,k,r):
    x[k] = 1
    if s+w[k] == m :
        print(x)
    elif (s+w[k]+w[k+1]) <= m :
        SumofSubset(s+w[k],k+1,r-w[k])
    
    if ((s+r-w[k]) >= m) and ((s+w[k+1]) <= m) :
        x[k] = 0 
        SumofSubset(s,k+1,r-w[k])

SumofSubset(0,0,sum(w))