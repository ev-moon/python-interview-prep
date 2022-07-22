# p.220

num_storages = int(input())
storages = list(map(int, input().split()))
max_plunder = 0
dp = [0] * num_storages
dp[0], dp[1] = storages[0], max(storages[0], storages[1])
for idx in range(2, num_storages):
    dp[idx] = max(dp[idx - 2] + storages[idx], dp[idx - 1])
print(dp[-1])
