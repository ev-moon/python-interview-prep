# p. 217

from collections import deque

# BFS
def solution(X):
    queue = deque([(X, 0)])
    while queue:
        number, num_ops = queue.popleft()
        if number == 1:
            return num_ops
        if number % 5 == 0:
            queue.append((number // 5, num_ops + 1))
        if number % 3 == 0:
            queue.append((number // 3, num_ops + 1))
        if number % 2 == 0:
            queue.append((number // 2, num_ops + 1))
        queue.append((number - 1, num_ops + 1))


# DP
def dp(X):
    d = [0] * 30001
    for i in range(2, X + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[X]


# other
def other(X):
    array = [float("inf")] * (X + 1)
    array[X] = 0

    pointer = X
    while pointer > 1:
        if pointer % 5 == 0:
            array[pointer // 5] = min(array[pointer] + 1, array[pointer // 5])
            pointer = pointer // 5
            continue
        if pointer % 3 == 0:
            array[pointer // 3] = min(array[pointer] + 1, array[pointer // 3])
            pointer = pointer // 3
            continue
        if pointer % 2 == 0:
            array[pointer // 2] = min(array[pointer] + 1, array[pointer // 2])
            pointer = pointer // 2
            continue
        array[pointer - 1] = min(array[pointer] - 1, array[pointer - 1])
        pointer -= 1
    return array[pointer]


print(solution())
