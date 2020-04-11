k = int(input())
table = [[k] for i in range(k)]
for i in range(k):
    table[i] = [int(s) for s in input().split()]

prec, rec = 0, 0
row_sum = [sum(row) for row in table]
column_sum = []
summ = sum(row_sum)
micro = 0
f = 0
for i in range(k):
    s = 0
    for j in range(k):
        s += table[j][i]
    column_sum.append(s)
for i in range(k):
    if column_sum[i] != 0:
        prec += table[i][i] * row_sum[i] / column_sum[i]
    else:
        prec = 0
    rec += table[i][i]

if (prec+rec) != 0:
    macro = (2 * (prec * rec) / (prec + rec))/summ
else:
    macro = 0
print(macro)

for i in range(k):
    if (column_sum[i] != 0) & (row_sum[i] != 0):
        prec = table[i][i]/column_sum[i]
        rec = table[i][i]/row_sum[i]
    else:
        prec = 0
        rec = 0
    if (prec+rec) != 0:
        f = 2*(prec*rec)/(prec+rec)
    else:
        f = 0
    micro += (row_sum[i] * f)/summ
print(micro)
