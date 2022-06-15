# p.339
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n_cities, n_roads, req_dist, start = map(int, input().strip().split())

roads = defaultdict(set)
for _ in range(n_roads):
    s, e = map(int, input().strip().split())
    roads[s].add(e)


def BFS(start, roads, req_dist):
    queue = deque([(start, 0)])
    min_dist = defaultdict(lambda: float("inf"))
    while queue:
        city, dist = queue.popleft()
        if dist > req_dist:
            break
        min_dist[city] = min(dist, min_dist[city])
        for next_city in roads[city]:
            if dist + 1 < min_dist[next_city]:
                queue.append((next_city, dist + 1))
    return min_dist


min_dist = BFS(start, roads, req_dist)
answer = [k for k, v in min_dist.items() if v == req_dist]

if answer:
    print(*sorted(answer), sep="\n")
else:
    print(-1)
