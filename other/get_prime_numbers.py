# p. 485
# https://www.acmicpc.net/problem/1929

import math

left_num, right_num = map(int, input().split())

is_prime = [True] * (right_num + 1)
is_prime[0], is_prime[1] = False, False
for i in range(2, int(math.sqrt(right_num)) + 1):
    if is_prime[i] == False:
        continue
    j = 2

    while i * j <= right_num:
        is_prime[i * j] = False
        j += 1

print(
    *[idx for idx in range(left_num, right_num + 1) if is_prime[idx] == True], sep="\n"
)
