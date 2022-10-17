from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(n)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([(0, 0, 0)])
while queue:
    x, y, answer = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(answer + 1)
        break
    if x < 0 or x >= n or y < 0 or y >= m:
        continue
    if maze[x][y] == 1:
        maze[x][y] = 0
        answer += 1
        for dx, dy in moves:
            queue.append((x + dx, y + dy, answer))
