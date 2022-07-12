# p. 367

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N, x = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)
print(-1 if left_index == right_index else right_index - left_index)


def binary_search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        answer = 1
        for idx in range(mid - 1, -1, -1):
            if array[idx] == target:
                answer += 1
        for idx in range(mid + 1, len(array)):
            if array[idx] == target:
                answer += 1
        return answer
    elif array[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(array, target, start, end)


print(binary_search(array, x, 0, len(array) - 1))
