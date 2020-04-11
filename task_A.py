# 10 4 3
# 1 2 3 4 1 2 3 1 2 1

n, m, k = [int(s) for s in input().split()]
list = [int(s) for s in input().split()]

ans = [[] for i in range(k)]
t = 0
for i in sorted(range(len(list)), key=lambda i: list[i]):
    ans[t].append(i+1)
    if t < k-1:
        t = t+1
    else:
        t = 0

for i in range(k):
    print(len(ans[i]), " ".join(map(str, sorted(ans[i]))))
