def binarray(n):
    binn = []
    for i in range(2**n):
        binn.append(bin(i)[2:])

    max_len = len(max(binn, key=len))
    for i in range(2**n):
        binn[i] = binn[i].zfill(max_len)
    return binn


m = int(input())
f = []

for i in range(2**m):
    f.append(int(input()))

arr = binarray(m)

if sum(f) != 0:
    print(2)
    print(sum(f), 1)
    for i in range(2 ** m):
        if f[i] == 1:
            num = 0
            for sym in arr[i]:
                if sym == "0":
                    print(-1.0, end=" ")
                else:
                    print(1.0, end=" ")
                    num += 1
            print(0.5 - num)
    for i in range(sum(f)):
        print(1, end=" ")
    print(-0.5)
else:
    print(1)
    print(1)
    for i in range(m):
        print(0, end=" ")
    print(-0.5)
