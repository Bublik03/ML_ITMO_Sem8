k1, k2 = [int(s) for s in input().split()]
n = int(input())
px1 = {}
px2 = {}
p = {}
x_2 = 0
for i in range(n):
    first, second = [int(s) for s in input().split()]
    if p.get((first-1, second-1)) is None:
        p[(first-1, second-1)] = 0
    p[(first-1, second-1)] += 1
    if px1.get(first-1) is None:
        px1[first-1] = 0
    px1[first-1] += 1/n
    if px2.get(second - 1) is None:
        px2[second - 1] = 0
    px2[second - 1] += 1 / n


for key in p.keys():
    ex = n * px1[key[0]] * px2[key[1]]
    if ex != 0:
        x_2 += (p[key] - ex)**2 / ex - ex
print(x_2+n)
