import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
lengths = list(map(int, input().strip().split()))
start = 0
end = max(lengths)
while start <= end:
    mid = (start + end) // 2
    cand = 0
    for length in lengths:
        cand += max(0, length - mid)
    if cand >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
