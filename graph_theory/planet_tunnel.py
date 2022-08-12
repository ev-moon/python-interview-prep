# p. 398
# https://www.acmicpc.net/problem/2887

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
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
    n_nodes = int(input().strip())
    x_list, y_list, z_list = [], [], []
    for i in range(n_nodes):
        x, y, z = map(int, input().strip().split())
        x_list.append((x, i))
        y_list.append((y, i))
        z_list.append((z, i))
    x_list.sort()
    y_list.sort()
    z_list.sort()
    edges = []
    for i in range(n_nodes - 1):
        edges.append(
            (abs(x_list[i][0] - x_list[i + 1][0]), x_list[i][1], x_list[i + 1][1])
        )
        edges.append(
            (abs(y_list[i][0] - y_list[i + 1][0]), y_list[i][1], y_list[i + 1][1])
        )
        edges.append(
            (abs(z_list[i][0] - z_list[i + 1][0]), z_list[i][1], z_list[i + 1][1])
        )

    edges.sort()
    parent = [i for i in range(n_nodes)]
    n_tunnels = 0
    total_cost = 0
    for info in edges:
        if n_tunnels == n_nodes - 1:
            break
        distance, a, b = info
        if find_parent(parent, a) != find_parent(parent, b):
            total_cost += distance
            n_tunnels += 1
            union_parent(parent, a, b)
    return total_cost


print(main())