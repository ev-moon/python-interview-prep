# p. 375

n_cases = int(input())
for _ in range(n_cases):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = [array[i * m : i * m + m] for i in range(n)]
    for i in range(1, m):
        for j in range(n):
            cands = []
            if j > 1:
                cands.append(dp[j - 1][i - 1])
            if j < n - 1:
                cands.append(dp[j + 1][i - 1])
            cands.append(dp[j][i - 1])
            dp[j][i] += max(cands)
    print(max([dp[i][m - 1] for i in range(n)]))
