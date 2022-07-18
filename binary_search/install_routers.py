# p. 369
# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

n_houses, n_routers = list(map(int, input().split()))
houses = [int(input().rstrip()) for _ in range(n_houses)]
houses.sort()

start = 1
end = houses[-1] - houses[0]
answer = 1

while start <= end:
    mid = (start + end) // 2
    pointer = houses[0]
    count = 1
    for i in range(1, n_houses):
        if houses[i] >= pointer + mid:
            pointer = houses[i]
            count += 1
    if count >= n_routers:
        start = mid + 1
        answer = mid
        continue
    end = mid - 1

print(answer)
