# https://www.acmicpc.net/problem/10825

import sys

input = sys.stdin.readline
N = int(input().strip())
score_list = []
for _ in range(N):
    name, s_1, s_2, s_3 = input().strip().split()
    score_list.append((name, int(s_1), int(s_2), int(s_3)))
score_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
print(*[l[0] for l in score_list], sep="\n")
