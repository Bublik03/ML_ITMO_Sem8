k = int(input())
n = int(input())
My, my = 0, 0
y = [0 for i in range(k)]
yp = [0 for i in range(k)]
for i in range(n):
    x, yc = [int(s) for s in input().split()]
    My += yc*yc / n
    y[x-1] += yc/n
    yp[x-1] += 1/n

for i in range(k):
    if yp[i] != 0:
        my += y[i]**2 / yp[i]
print(My - my)