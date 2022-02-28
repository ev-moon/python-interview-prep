n_rows, _ = map(int, input().split())

answer = 1
for _ in range(n_rows):
    array = list(map(int, input().split()))
    answer = max(answer, min(array))

print(answer)