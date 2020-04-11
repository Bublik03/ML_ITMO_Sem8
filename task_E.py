from math import log, exp

k = int(input())
lam = [int(s) for s in input().split()]
a = int(input())
n = int(input())
c = [0 for i in range(k)]
class_words = [{} for i in range(k)]
Allwords = set()
for i in range(n):
    line = input().split()
    for word in set(line[2:]):
        Allwords.add(word)
        if class_words[int(line[0])-1].get(word) is None:
            class_words[int(line[0])-1][word] = 1.0
        else:
            class_words[int(line[0])-1][word] += 1.0
    c[int(line[0])-1] += 1

for i in range(k):
    for word in Allwords:
        if class_words[i].get(word) is None:
            class_words[i][word] = 0.0
        class_words[i][word] = (a + class_words[i][word]) / (c[i] + a*2)

logs = {i: dict() for i in range(k)}
logs1 = {i: dict() for i in range(k)}

for i in range(k):
    for word in Allwords:
        logs[i][word] = log(class_words[i][word])
        logs1[i][word] = log(1 - class_words[i][word])

m = int(input())
p = [0.0 for i in range(k)]
for l in range(m):
    line = set(input().split()[1:])
    for i in range(k):
        p[i] = 0.0
        if c[i] == 0.0:
            p[i] = 0.0
        else:
            for word in Allwords:
                if word in line:
                    if class_words[i][word] == 0.0:
                        p[i] = 0.0
                        break
                    else:
                        p[i] += logs[i][word]
                else:
                    p[i] += logs1[i][word]
            p[i] += log(c[i] / n)
    maxp = max(p)
    for i in range(k):
        if p[i] != 0.0:
            p[i] = exp(p[i]-maxp) * lam[i]
    summa = sum(p)
    for i in range(k):
        print(p[i] / summa, end=" ")
    print()