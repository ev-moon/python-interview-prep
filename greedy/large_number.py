_, M, K = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort()

largest = array[-1]
second_largest = array[-2]

# answer = it = 0

# while it < M:
#     answer += largest * min(K, M - it)
#     it += min(K, M - it)
#     if it < M:
#         answer += second_largest
#         it += 1
div, mod = divmod(M, K + 1)
answer = (array[-1] * K + array[-2]) * div + array[-1] * mod

print(answer)