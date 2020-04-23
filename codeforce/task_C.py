import math

n, m = [int(s) for s in input().split()]
d = [[m + 1] for i in range(n)]

for i in range(n):
    d[i] = [int(s) for s in input().split()]
q = [int(s) for s in input().split()]
dis = input()
ker = input()
win = input()
h = int(input())


def uniform(u):
    if abs(u) < 1:
        return 1 / 2
    return 0


def triangular(u):
    if abs(u) < 1:
        return (1 - abs(u))
    return 0


def epanechnikov(u):
    if abs(u) < 1:
        return (1 - u ** 2) * 3 / 4
    return 0


def quartic(u):
    if abs(u) < 1:
        return ((1 - u ** 2) ** 2) * 15 / 16
    return 0


def triweight(u):
    if abs(u) < 1:
        return ((1 - u ** 2) ** 3) * 35 / 32
    return 0


def tricube(u):
    if abs(u) < 1:
        return ((1 - abs(u) ** 3) ** 3) * 70 / 81
    return 0


def gaussian(u):
    return math.e ** ((-1 / 2) * u ** 2) / (2 * math.pi) ** (1 / 2)


def cosine(u):
    if abs(u) < 1:
        return (math.pi / 4) * math.cos(u * math.pi / 2)
    return 0


def logistic(u):
    return 1 / (math.e ** u + 2 + math.e ** (-u))


def sigmoid(u):
    return 2 / (math.pi * (math.e ** u + math.e ** (-u)))


kernel = {
    "uniform": uniform,
    "triangular": triangular,
    "epanechnikov": epanechnikov,
    "quartic": quartic,
    "triweight": triweight,
    "tricube": tricube,
    "gaussian": gaussian,
    "cosine": cosine,
    "logistic": logistic,
    "sigmoid": sigmoid
}


def manhattan(p, q):
    summa = 0
    for i in range(m):
        summa += abs(p[i] - q[i])
    return summa


def euclidean(p, q):
    summa = 0
    for i in range(m):
        summa += (p[i] - q[i]) ** 2
    return summa ** (1 / 2)


def chebyshev(p, q):
    maxs = 0
    for i in range(m):
        if maxs < abs(p[i] - q[i]):
            maxs = abs(p[i] - q[i])
    return maxs


distances = {
    "manhattan": manhattan,
    "euclidean": euclidean,
    "chebyshev": chebyshev
}

dists = []
means = []

for i in d:
    dists.append((distances[dis](i[:-1], q), i[-1]))


dists = sorted(dists, key=lambda x: x[0])

def kersss(distances, meanes):
    kers = []
    kers_mean = []
    answer = 0
    count = 0
    for i in range(n):
        if distances[i] != 0 and (h == 0 or (win == "variable" and distances[h] == 0)):
            kers.append(0)
            kers_mean.append(0)
        elif h == 0 and (0 not in distances):
            return sum(meanes) / n
        elif h == 0 and (0 in distances):
            if distances[i] == 0:
                count += 1
                answer += means[i]
        else:
            if win == "fixed":
                u = distances[i] / h
            else:
                if distances[h] != 0:
                    u = distances[i] / distances[h]
                else:
                    u = 0
            kers.append(kernel[ker](u))
            kers_mean.append(meanes[i] * kernel[ker](u))
    if count != 0:
        return answer / count
    if sum(kers) != 0:
        return sum(kers_mean) / sum(kers)
    else:
        return sum(meanes) / n


for i in range(n):
    means.append(dists[i][1])
    dists[i] = dists[i][0]

ans = kersss(dists, means)
print(ans)