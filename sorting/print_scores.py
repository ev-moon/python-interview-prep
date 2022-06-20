# p.180

N = int(input())
score_list = [[] for _ in range(100)]

for _ in range(N):
    name, score = input().split()
    score_list[int(score) - 1].append(name)
for names in score_list:
    if names:
        print(*names, end=" ")
