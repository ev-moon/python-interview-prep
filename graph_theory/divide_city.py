# p. 300
# https://www.acmicpc.net/problem/1647

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


n_nodes, n_edges = map(int, input().strip().split())
parent = [i for i in range(n_nodes + 1)]
edges = []
for _ in range(n_edges):
    a, b, cost = map(int, input().strip().split())
    edges.append((cost, a, b))
edges.sort()
total_cost = 0
last_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    total_cost += cost
    last_cost = cost
print(total_cost - last_cost)
