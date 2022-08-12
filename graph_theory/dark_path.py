# p. 397

import sys

input = sys.stdin.readline


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
    n_nodes, n_edges = map(int, input().strip().split())
    edges = []
    parent = [i for i in range(n_nodes)]
    for _ in range(n_edges):
        a, b, cost = map(int, input().strip().split())
        edges.append((cost, a, b))
    saved_cost = 0
    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b):
            saved_cost += cost
            continue
        union_parent(parent, a, b)
    return saved_cost


print(main())