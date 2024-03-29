n = 8
x = [0,0,0,0,0,0,0,0]

def NQueens(k,n):
    for i in range(n):
        if place(k,i): 
            x[k] = i 
            if k==n-1: 
               print(x)
            else: 
               NQueens(k+1,n)
        
def place(k,i):
    for j in range(k):
        if (x[j] == i) or (abs(j-k) == abs(x[j]-i)) : 
            return False
    return True
    
NQueens(0,n)