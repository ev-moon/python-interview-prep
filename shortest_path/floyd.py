# p. 385
# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

n_nodes = int(input().rstrip())
n_edges = int(input().rstrip())

min_dist = [[float("inf")] * (n_nodes + 1) for _ in range(n_nodes + 1)]
for i in range(1, n_nodes + 1):
    min_dist[i][i] = 0

for _ in range(n_edges):
    s, e, cost = map(int, input().split())
    min_dist[s][e] = min(min_dist[s][e], cost)


for k in range(1, n_nodes + 1):
    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            min_dist[i][j] = min(min_dist[i][j], min_dist[i][k] + min_dist[k][j])

for i in range(1, n_nodes + 1):
    for j in range(1, n_nodes + 1):
        print(0 if min_dist[i][j] == float("inf") else min_dist[i][j], end=" ")
    print()
