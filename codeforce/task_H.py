def thn(m):
    from math import tanh
    m3 = []
    for i in range(len(m)):
        m3.append([])
        for j in range(len(m[0])):
            m3[i].append(tanh(m[i][j]))
    return m3


def tnh_inv(m):
    from math import cosh
    m3 = []
    for i in range(len(m)):
        m3.append([])
        for x in m[i]:
            m3[i].append(1 / (cosh(x) * cosh(x)))
    return m3


def rlu(m, alpha):
    m3 = []
    for i in range(len(m)):
        m3.append([])
        for j in range(len(m[0])):
            if m[i][j] >= 0:
                m3[i].append(m[i][j])
            else:
                m3[i].append(m[i][j] / alpha)
    return m3


def rlu_inv(m, alpha):
    m3 = []
    for row in range(len(m)):
        m3.append([])
        for x in m[row]:
            if x >= 0:
                m3[row].append(1.0)
            else:
                m3[row].append(1 / alpha)
    return m3


def mul(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
            for k in range(len(m1[0])):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3


def summ(matrs):
    m3 = []
    for row in range(len(matrs[0])):
        m3.append([])
        for col in range(len(matrs[0][0])):
            m3[row].append(0)
            for k in range(len(matrs)):
                m3[row][col] += matrs[k][row][col]
    return m3


def had(matrs):
    m3 = []
    for row in range(len(matrs[0])):
        m3.append([])
        for col in range(len(matrs[0][0])):
            m3[row].append(1)
            for k in range(len(matrs)):
                m3[row][col] *= matrs[k][row][col]
    return m3


def new_m(rows, cols, init):
    return [[init] * cols for i in range(rows)]


def transpose(matr):
    m3 = []
    for i in range(len(matr[0])):
        m3.append([])
        for j in range(len(matr)):
            m3[i].append(matr[j][i])
    return m3


n, m, k = [int(s) for s in input().split()]
nodes_desc = []
nodes_d = []
for i in range(n):
    line = input().split()
    nodes_desc.append((line[0], list(map(int, line[1:]))))
nodes = []
for i in range(m):
    nodes.append([])
    nodes_d.append(new_m(nodes_desc[i][1][0], nodes_desc[i][1][1], 0.0))
    for row in range(nodes_desc[i][1][0]):
        nodes[i].append([int(s) for s in input().split()])

# if k + m > n:
#     for i in range(n - k, m):
#         nodes_d[i] = list(map(float, input().split()))
#         for row in nodes[i]:
#             print(*row)
# print(nodes)
for i in range(n + 1 - m - k, n):
    cur_node = nodes_desc[i]
    if cur_node[0] == 'tnh':
        idd = cur_node[1][0] - 1
        nodes.append(thn(nodes[idd]))
    elif cur_node[0] == 'rlu':
        idd = cur_node[1][1] - 1
        alp = cur_node[1][0]
        nodes.append(rlu(nodes[idd], alp))
    elif cur_node[0] == 'mul':
        idd1 = cur_node[1][0] - 1
        idd2 = cur_node[1][1] - 1
        nodes.append(mul(nodes[idd1], nodes[idd2]))
    elif cur_node[0] == 'sum':
        nodes_to_sum = [nodes[j - 1] for j in cur_node[1][1:]]
        nodes.append(summ(nodes_to_sum))
    elif cur_node[0] == 'had':
        nodes_to_had = [nodes[j - 1] for j in cur_node[1][1:]]
        nodes.append(had(nodes_to_had))

    r, c = len(nodes[-1]), len(nodes[-1][0])
    if i < n - k:
        nodes_d.append(new_m(r, c, 0.0))
    else:
        nodes_d.append([[float(x) for x in input().split()] for i in range(r)])

# for i in range(k):
#     nodes_d[i] = []
#     for row in range(len(nodes[n - 1 - i])):
#         nodes_d[i].append([int(s) for s in input().split()])

# for node in nodes:
#     print('__________________________')
#     for row in node:
#         print(row)
#     print('__________________________')


for i in range(n - 1, m - 1, -1):
    cur_node = nodes_desc[i]
    if cur_node[0] == 'tnh':
        idd = cur_node[1][0] - 1
        nodes_d[idd] = summ([nodes_d[idd], had([tnh_inv(nodes[idd]), nodes_d[i]])])
    elif cur_node[0] == 'rlu':
        idd = cur_node[1][1] - 1
        nodes_d[idd] = summ([nodes_d[idd], had([rlu_inv(nodes[idd], cur_node[1][0]), nodes_d[i]])])
    elif cur_node[0] == 'mul':
        idd1 = cur_node[1][0] - 1
        idd2 = cur_node[1][1] - 1
        nodes_d[idd1] = summ([nodes_d[idd1], mul(nodes_d[i], transpose(nodes[idd2]))])
        nodes_d[idd2] = summ([nodes_d[idd2], mul(transpose(nodes[idd1]), nodes_d[i])])
    elif cur_node[0] == 'sum':
        for it in cur_node[1][1:]:
            idd = it - 1
            nodes_d[idd] = summ([nodes_d[idd], nodes_d[i]])
    elif cur_node[0] == 'had':
        idds = [x - 1 for x in cur_node[1][1:]]
        if len(idds) > 1:
            for ind_of_matrix, matrix_ind in enumerate(idds, 0):
                idds = idds[:ind_of_matrix] + idds[ind_of_matrix + 1:]
                matrices = [nodes[i] for i in idds]
                matrices.append(nodes_d[i])
                nodes_d[matrix_ind] = summ([nodes_d[matrix_ind], had(matrices)])
        else:
            nodes_d[idds[0]] = summ([nodes_d[idds[0]], nodes_d[i]])

for i in range(k):
    for row in nodes[n - 1 - i]:
        print(*row)
for i in range(m):
    for row in nodes_d[i]:
        print(*row)