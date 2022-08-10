# p. 303

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0]
indegree = [0] * (n + 1)
for idx in range(n):
    class_info = list(map(int, input().split()))
    class_time, prereq = class_info[0], class_info[1:-1]
    indegree[idx + 1] = len(prereq)
    time.append(class_time)
    for node in prereq:
        graph[node].append(idx + 1)

queue = deque([(time[i], i) for i in range(1, n + 1) if indegree[i] == 0])
total_time = {}
while queue:
    cur_time, node = queue.popleft()
    total_time[node] = cur_time
    for n_node in graph[node]:
        indegree[n_node] -= 1
        if indegree[n_node] == 0:
            queue.append((cur_time + time[n_node], n_node))

print(*[value for key, value in sorted(total_time.items())], sep="\n")