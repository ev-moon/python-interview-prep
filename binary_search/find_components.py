import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


input = sys.stdin.readline

N = int(input().strip())
inventory = list(map(int, input().rstrip().split()))
inventory.sort()

M = int(input().strip())
order = list(map(int, input().strip().split()))
for item in order:
    if binary_search(inventory, item, 0, len(inventory) - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
