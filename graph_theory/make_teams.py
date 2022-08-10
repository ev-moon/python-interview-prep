# p. 298


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n_students, n_ops = map(int, input().split())
n_students += 1
parent = [i for i in range(n_students)]
for _ in range(n_ops):
    op, a, b = map(int, input().split())
    if op == 0:  # union
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")