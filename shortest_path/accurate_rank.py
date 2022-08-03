# p. 386

n_students, n_comparisons = map(int, input().split())
graph = [[float("inf")] * (n_students + 1) for _ in range(n_students + 1)]
for i in range(n_students + 1):
    graph[i][i] = 0
for _ in range(n_comparisons):
    s, e = map(int, input().split())
    graph[s][e] = 1

for k in range(1, n_students + 1):
    for i in range(1, n_students + 1):
        for j in range(1, n_students + 1):
            if graph[i][k] != float("inf") and graph[k][j] != float("inf"):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, n_students + 1):
    for j in range(1, n_students + 1):
        if graph[i][j] == float("inf") and graph[j][i] == float("inf"):
            answer -= 1
            break
    answer += 1

print(answer)
