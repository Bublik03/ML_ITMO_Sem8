from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

m, k, h = list(map(int, input().split()))
idd = 0
n = int((input()))
dataset = []
for i in range(n):
    dataset.append(list(map(int, input().split())))




def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0.0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini


def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_score = 999.0
    global idd
    idd += 1
    por = len(dataset[0]) - 1
    for index in range(por):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index = index
                b_value = row[index] - 0.5
                b_score = gini
                b_groups = groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups, 'id': idd}


def to_terminal(group):
    outcomes = [row[-1] for row in group]
    global idd
    idd += 1
    return {'class': max(set(outcomes), key=outcomes.count), 'id': idd}


def split(node, max_depth, depth):
    left, right = node['groups']
    del (node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(list(set(row[-1] for row in left))) == 1:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, depth + 1)
    if len(list(set(row[-1] for row in right))) == 1:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, depth + 1)


def print_tree(node):
    if node.get('left') is None:
        print('C', end=' ')
        print(node['class'])
    else:
        print('Q', end=' ')
        print(node['index'] + 1, end=' ')
        print(node['value'], end=' ')
        print(node['left']['id'], end=' ')
        print(node['right']['id'])
        print_tree(node['left'])
        print_tree(node['right'])


isOneClass = True
for row in dataset[1:]:
    if row[-1] != dataset[0][-1]:
        isOneClass = False
        break
if k == 1 or isOneClass:
    print('C ', dataset[0][-1])
    exit()


tree = get_split(dataset)
split(tree, h, 1)
# print(tree)
print(idd)
print_tree(tree)

# dataset = [[2.771244718,1.784783929,0],
# 	[1.728571309,1.169761413,0],
# 	[3.678319846,2.81281357,0],
# 	[3.961043357,2.61995032,0],
# 	[2.999208922,2.209014212,0],
# 	[7.497545867,3.162953546,1],
# 	[9.00220326,3.339047188,1],
# 	[7.444542326,0.476683375,1],
# 	[10.12493903,3.234550982,1],
# 	[6.642287351,3.319983761,1]]
