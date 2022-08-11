# p. 395


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


def main():
    n_gates = int(input())
    n_planes = int(input())

    info = [int(input()) for _ in range(n_planes)]
    parent = [i for i in range(n_gates + 1)]
    docked = 0
    for target in info:
        data = find_parent(parent, target)
        if data == 0:
            break
        union_parent(parent, data, data - 1)
        docked += 1
    return docked


print(main())