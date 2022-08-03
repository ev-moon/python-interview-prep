import heapq

n_cases = int(input())

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for _ in range(n_cases):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(size)]
    start = (0, 0)
    queue = [(graph[0][0], start)]
    heapq.heapify(queue)
    min_dist = [[float("inf")] * size for _ in range(size)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist < min_dist[node[0]][node[1]]:
            min_dist[node[0]][node[1]] = dist
            for dx, dy in moves:
                nx, ny = node[0] + dx, node[1] + dy
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    continue
                new_cost = dist + graph[nx][ny]
                if new_cost < min_dist[nx][ny]:
                    heapq.heappush(queue, (new_cost, (nx, ny)))
    print(min_dist[-1][-1])
