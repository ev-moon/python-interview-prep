from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(n)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(maze[x][y])
        break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
