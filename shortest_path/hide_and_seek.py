# p. 390

import heapq, sys

input = sys.stdin.readline

n_nodes, n_edges = map(int, input().rstrip().split())
graph = [set() for _ in range(n_nodes + 1)]
for _ in range(n_edges):
    n1, n2 = map(int, input().rstrip().split())
    graph[n1].add(n2)
    graph[n2].add(n1)
min_dist = [float("inf") for _ in range(n_nodes + 1)]
queue = [(0, 1)]
heapq.heapify(queue)

while queue:
    dist, node = heapq.heappop(queue)
    if min_dist[node] > dist:
        min_dist[node] = dist
        for n_node in graph[node]:
            if min_dist[n_node] > dist + 1:
                heapq.heappush(queue, (dist + 1, n_node))

answer = [1]
longest_dist = 0

for idx in range(2, n_nodes + 1):
    if longest_dist < min_dist[idx]:
        answer = [idx]
        longest_dist = min_dist[idx]
    elif min_dist[idx] == longest_dist:
        answer.append(idx)
print(answer[0], longest_dist, len(answer))
