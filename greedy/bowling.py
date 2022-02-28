from collections import Counter

n, m = map(int, input().split())

balls = list(map(int, input().split()))
counter = Counter(balls)

answer = 0
remaining = n

for num in range(1, m + 1):
    answer += counter[num] * (remaining - counter[num])
    remaining -= counter[num]

print(answer)