n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0


def dfs(x, y):
    if not 0 <= x < n or not 0 <= y < m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for dx, dy in moves:
            dfs(x + dx, y + dy)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1
print(answer)
