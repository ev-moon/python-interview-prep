# p. 395


def update_parent(parent, target, visited):
    while parent[target] in visited:
        if parent[target] == 1:
            return True  # cannot dock
        parent[target] = find_parent(parent, parent[target] - 1)
    return False  # can dock


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def main():
    n_gates = int(input())
    n_planes = int(input())

    info = [int(input()) for _ in range(n_planes)]
    parent = [i for i in range(n_gates + 1)]

    visited = set()
    docked = 0
    for target in info:
        if update_parent(parent, target, visited):
            break
        visited.add(parent[target])
        docked += 1
    return docked


print(main())