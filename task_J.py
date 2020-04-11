n = int(input())
x1 = []
x2 = []
d = 0
for i in range(n):
    first, second = input().split()
    x1.append(int(first))
    x2.append(int(second))

x11 = dict(zip(sorted(x1), range(1, len(x1)+1)))
x22 = dict(zip(sorted(x2), range(1, len(x2)+1)))

for i in range(n):
    d += (x11.get(x1[i]) - x22.get(x2[i]))**2

if n == 1:
    p = 1
else:
    p = 1 - 6 * d / (n ** 3 - n)
print(p)
