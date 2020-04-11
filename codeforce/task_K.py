k = int(input())
n = int(input())
x_all = []
classes = [[] for i in range(k)]
v, m = 0, 0
for i in range(n):
    first, second = input().split()
    x_all.append(int(first))
    classes[int(second) - 1].append(int(first))

for x_part in classes:
    x_part.sort()
    for i in range(1, len(x_part)+1):
        v += x_part[len(x_part)-i]*(len(x_part)-i)*2 - x_part[len(x_part)-i]*(len(x_part)-1)

print(2 * v)
x_all.sort()
for i in range(1, len(x_all)+1):
    m += x_all[len(x_all)-i]*(len(x_all)-i)*2 - x_all[len(x_all)-i]*(len(x_all)-1)
print(2*(m-v))