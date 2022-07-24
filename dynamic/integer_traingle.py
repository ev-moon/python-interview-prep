# p. 376

import sys

input = sys.stdin.readline

t_size = int(input().strip())
array = [list(map(int, input().strip().split())) for _ in range(t_size)]
for i in range(1, t_size):
    for j in range(len(array[i])):
        cands = []
        if j > 0:
            cands.append(array[i - 1][j - 1])
        if j != len(array[i]) - 1:
            cands.append(array[i - 1][j])
        array[i][j] += max(cands)
print(max(array[t_size - 1]))
