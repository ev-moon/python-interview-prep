# p. 259

import sys
import heapq

input = sys.stdin.readline

n_nodes, n_edges = map(int, input().split())
graph = [set() for _ in range(n_nodes + 1)]
min_dist = float()
for _ in range(n_edges):
    s, e = map(int, input().split())
    graph[s].add(e)
    graph[e].add(s)


def dijkstra(start, end):
    queue = [(0, start)]
    min_dist = [float("inf")] * (n_nodes + 1)
    heapq.heapify(queue)
    while queue:
        dist, node = heapq.heappop(queue)
        if min_dist[node] > dist:
            min_dist[node] = dist
            for n_node in graph[node]:
                if dist + 1 < min_dist[n_node]:
                    heapq.heappush(queue, (dist + 1, n_node))
    return min_dist[end]


def floyd_warshall():
    min_dist = [[float("inf")] * (n_nodes + 1) for _ in range(n_nodes + 1)]
    for node in range(1, len(graph)):
        for c_node in graph[node]:
            min_dist[node][c_node] = 1
            min_dist[c_node][node] = 1
    for i in range(n_nodes + 1):
        min_dist[i][i] = 0
    for k in range(1, n_nodes + 1):
        for i in range(1, n_nodes + 1):
            for j in range(1, n_nodes + 1):
                if k in graph[i] and j in graph[k]:
                    min_dist[i][j] = min(
                        min_dist[i][j], min_dist[i][k] + min_dist[k][j]
                    )
    return min_dist


X, K = map(int, input().split())

# 다익스트라 풀이
# total_distance = dijkstra(1, K) + dijkstra(K, X)

# 플로이드 워셜 풀이
min_dist = floyd_warshall()
total_distance = min_dist[1][K] + min_dist[K][X]

print(-1 if total_distance == float("inf") else total_distance)
