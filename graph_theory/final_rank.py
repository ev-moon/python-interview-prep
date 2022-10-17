# p. 399
# https://www.acmicpc.net/problem/3665

from collections import deque


def topology_sort(graph, indegree):
    queue = deque([i for i in range(1, n_teams + 1) if indegree[i] == 0])
    result = []
    for _ in range(n_teams):
        if len(queue) >= 2:
            return "?"
        if not queue:
            return "IMPOSSIBLE"
        team = queue.popleft()
        result.append(team)
        to_append = []
        for idx in range(len(graph)):
            if graph[team][idx]:
                indegree[idx] -= 1
                if indegree[idx] == 0:
                    queue.append(idx)
    return " ".join([str(item) for item in result])


n_cases = int(input())
for _ in range(n_cases):
    n_teams = int(input())
    indegree = [0] * (n_teams + 1)
    rank = list(map(int, input().split()))
    graph = [[False] * (n_teams + 1) for _ in range(n_teams + 1)]
    for i in range(n_teams):
        for j in range(i + 1, n_teams):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1
    n_changes = int(input())
    for _ in range(n_changes):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1
    print(topology_sort(graph, indegree))
