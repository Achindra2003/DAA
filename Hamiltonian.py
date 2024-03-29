G = [[ 0, 10, 15, 20 ],
     [ 10, 0, 35, 25 ],
     [ 15, 35, 0, 30 ],
     [ 20, 25, 30, 0 ]]
n = 4
x = [0, 0, 0, 0]

def Hamiltonian(k):
    while True:
        NextValue(k)
        if x[k] == 0:
            return
        if k == n - 1:
            print(x)
        else:
            Hamiltonian(k + 1)

def NextValue(k):
    while True:
        x[k] = (x[k] + 1) % (n + 1)
        if x[k] == 0:
            return
        if G[x[k-1]-1][x[k]-1] != 0:
            j = 0
            while j < k :
                if x[j] == x[k]:
                    break
                j += 1

            if j == k:
                if k < n-1 or (k == n-1 and G[x[n-1]-1][x[0]-1] != 0):
                    return

Hamiltonian(0)
