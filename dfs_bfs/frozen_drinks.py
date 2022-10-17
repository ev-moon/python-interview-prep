N, M = map(int, input().strip().split())

graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
stack = [(0, 0)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0


def find_next_unvisited():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                return (i, j)
    return (-1, -1)


def dfs(stack, answer, traversed=0):
    x, y = stack.pop()
    if not visited[x][y]:
        visited[x][y] = True
        if graph[x][y] == 1:
            traversed += 1
            for dx, dy in moves:
                if 0 <= x + dx < N and 0 <= y + dy < M:
                    stack.append((x + dx, y + dy))
    if not stack:
        if traversed != 1:
            answer += 1
        return
    dfs(stack, answer, traversed)


while True:
    stack = [find_next_unvisited()]
    if stack[0] == (-1, -1):
        print(answer)
        break
    dfs(stack, answer)
