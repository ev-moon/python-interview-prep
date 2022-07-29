# p. 567
# https://www.acmicpc.net/problem/14501

n_days = int(input())
info = [list(map(int, input().split())) for _ in range(n_days)]
dp = [0] * n_days
if info[0][0] == 1:
    dp[0] = info[0][1]
for i in range(n_days):
    dp[i] = max(dp[i - 1], dp[i])
    if info[i][0] == 1 and i != 0:
        dp[i] = max(dp[i - 1] + info[i][1], dp[i])
    elif info[i][0] + i <= n_days and info[i][0] != 1:
        dp[info[i][0] + i - 1] = max(dp[info[i][0] + i - 1], dp[i - 1] + info[i][1])

print(dp[-1])

# solution
max_value = 0
dp = [0] * (n_days + 1)
for i in range(n_days - 1, -1, -1):
    time = info[i][0] + i
    if time <= n_days:
        dp[i] += max(info[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
