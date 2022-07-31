# p. 262

import sys
import heapq

input = sys.stdin.readline
n_node, n_edge, start = map(int, input().split())
graph = list(dict() for _ in range(n_node + 1))
for _ in range(n_edge):
    s, e, cost = map(int, input().split())
    graph[s][e] = cost

min_dist = [float("inf")] * (n_node + 1)
queue = [(0, start)]
heapq.heapify(queue)
time = 0
while queue:
    dist, city = heapq.heappop(queue)
    time = max(time, dist)
    if min_dist[city] > dist:
        min_dist[city] = dist
        for (n_node, n_dist) in graph[city].items():
            if dist + n_dist < min_dist[n_node]:
                heapq.heappush(queue, (dist + n_dist, n_node))

print(n_node - min_dist.count(float("inf")), time)
