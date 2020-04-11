def matrixmult(m1,m2):
    s = 0
    t = []
    m3 = []
    r1 = len(m1)
    c1 = len(m1[0])
    c2 = len(m2[0])
    for z in range(r1):
        for j in range(c2):
            for i in range(c1):
                s += m1[z][i]*m2[i][j]
            t.append(s)
            s = 0
        m3.append(t)
        t = []
    return m3


n, m = [int(s) for s in input().split()]
F = []
F_T = [[0 for i in range(n)] for j in range(m)]
y = []

for i in range(n):
    line = [int(s) for s in input().split()]
    F.append(line[:-1])
    y.append(line[m])
for i in range(n):
    for j in range(m):
        F_T[j][i] = F[i][j]
print(F_T)

