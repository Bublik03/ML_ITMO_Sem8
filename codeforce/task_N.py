import math

kx, ky = [int(s) for s in input().split()]
n = int(input())
p = {}
px = [0 for i in range(kx)]
py = {}
h = 0
for i in range(n):
    first, second = [int(s) for s in input().split()]
    if p.get((first - 1, second - 1)) is None:
        p[(first - 1, second - 1)] = 0
    p[(first - 1, second - 1)] += 1 / n
    px[first - 1] += 1 / n
    if py.get(second-1) is None:
        py[second-1] = 0
    py[second-1] += 1

for (x, y), val in p.items():
    h += px[x] * (p[(x, y)] / px[x]) * math.log(p[(x, y)] / px[x])

# for xi in px:
#     h_ = 0
#     for (x, y), val in p.items():
#             h_ += xi * (p[(px.index(xi), y)] / xi) * math.log(p[(px.index(xi), y)] / xi)

print(-h)
