# p. 568
# https://www.acmicpc.net/problem/18353

N = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * N
soldiers.reverse()

for i in range(1, N):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
