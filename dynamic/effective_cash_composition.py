# p. 226
n_types, target_sum = map(int, (input().split()))
units = [int(input()) for _ in range(n_types)]

dp = [float("inf")] * (target_sum + 1)
dp[0] = 0  # 첫번째 인덱스 0으로 초기화 주의
for idx in range(1, target_sum + 1):
    for unit in units:
        if idx - unit >= 0:
            dp[idx] = min(dp[idx], dp[idx - unit] + 1)
print(-1 if dp[-1] == float("inf") else dp[target_sum])
