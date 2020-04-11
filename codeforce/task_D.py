import math

n, m = [int(s) for s in input().split()]
d = [[m+1] for i in range(n)]

for i in range(n):
    d[i] = [int(s) for s in input().split()]
q = [int(s) for s in input().split()]
dis = input()
ker = input()
win = input()
h = int(input())


def uniform(u):
    if abs(u) <= 1:
        return 1/2
    return 0


def triangular(u):
    if abs(u) <= 1:
        return(1-abs(u))
    return 0


def epanechnikov(u):
    if abs(u) <= 1:
        return (1-u**2)*3/4
    return 0


def quartic(u):
    if abs(u) <= 1:
        return ((1-u**2)**2) * 15/16
    return 0


def triweight(u):
    if abs(u) <= 1:
        return ((1-u**2)**3) * 35/32
    return 0


def tricube(u):
    if abs(u) <= 1:
        return (1-abs(u)**3)**3
    return 0


def gaussian(u):
    return math.e**((-1/2)*u**2)/(2*math.pi)**(1/2)


def cosine(u):
    if abs(u) <= 1:
        return (math.pi/4) * math.cos(u*math.pi/2)
    return 0


def logistic(u):
    return 1/(math.e**u + 2 + math.e**(-u))


def sigmoid(u):
    return 2/(math.pi*(math.e**u + math.e**(-u)))

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
        summa += (p[i] - q[i])**2
    return summa**(1/2)


def chebyshev(p, q):
    maxs = 0
    for i in range(m):
        if maxs < (p[i] - q[i]):
            maxs = p[i] - q[i]
    return maxs


distances = {
    "manhattan": manhattan,
    "euclidean": euclidean,
    "chebyshev": chebyshev
}

dists = []
means = []

for i in d:
    dists.append(distances[dis](i, q))
    means.append(i[m])

kers = []
kers_mean = []

for i in range(n):
    if win == "fixed":
        if h != 0:
            u = dists[i] / h
        else:
            u = 0
    else:
        if dists[h] != 0:
            u = dists[i] / dists[h]
        else:
            u = 0
    kers.append(kernel[ker](u))
    kers_mean.append(means[i]*kernel[ker](u))

print(sum(kers_mean)/sum(kers))