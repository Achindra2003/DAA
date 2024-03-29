G = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
n = 4
m = 3
x = [0, 0, 0, 0]

def mColoring(k):
    while True:
        NextValue(k)
        if x[k] == 0:
            return
        if k == n - 1:
            print(x)
        else:
            mColoring(k + 1)

def NextValue(k):
    while True:
        x[k] = (x[k] + 1) % (m + 1)
        if x[k] == 0:
            return
        j = 0
        while j < n:
            if G[k][j] != 0 and x[j] == x[k]:
                break
            j += 1
        if j == n:
            return

mColoring(0)
