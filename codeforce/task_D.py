import random

n, m = [int(s) for s in input().split()]
x = []
y = []
ans = []
for i in range(n):
    line = [int(s) for s in input().split()]
    x.append(line[:-1])
    y.append(line[m])

if m == 1:
    ans.append((n * sum(x[i][0]*y[i] for i in range(n)) - sum(x[i][0] for i in range(n)) * sum(y))/(n * sum(l[0]*l[0] for l in x) - sum(x[i][0] for i in range(n))*sum(x[i][0] for i in range(n))))
    ans.append((sum(y) - ans[0] * sum(x[i][0] for i in range(n))) / n)
    for i in ans:
        print(i)
    exit()

for xx in x:
    xx.append(1)
for i in range(m+1):
    ans.append(-1/(2*(m+1)) + random.random()/m+1)

alp = 0
for i in range(10000):
    new_i = round(random.random() * n)
    if new_i > n-1:
        new_i = n-1
    preY = 0
    for j in range(m+1):
        preY += ans[j] * x[new_i][j]
    diff = preY + x[new_i][m] - y[new_i]
    rto = []
    for j in range(m+1):
        rto.append(2*diff * x[new_i][j])
    dx = 0
    for j in range(m+1):
        dx += rto[j] * x[new_i][j]
    dx += x[new_i][m]
    if dx != 0:
        alp = diff / dx
    else:
        continue
    for j in range(m+1):
        ans[j] -= alp * rto[j]
for an in ans:
    print(an)