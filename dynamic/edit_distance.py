original = input()
target = input()

dp = [[0] * (len(target) + 1) for _ in range(len(original) + 1)]
dp[0] = [_ for _ in range(len(target) + 1)]
for i in range(1, len(original) + 1):
    dp[i][0] = i

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if original[i - 1] == target[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
