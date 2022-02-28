# p.311

n = int(input())
fear_array = list(map(int, input().split()))
fear_array.sort()

answer = 0
group_start = 0
for idx, fear in enumerate(fear_array):
    if fear <= idx - group_start + 1:
        answer += 1
        group_start = idx + 1

print(answer)